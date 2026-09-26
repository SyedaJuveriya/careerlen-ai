from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, redirect, session

from db import Base, engine, SessionLocal
import models
from ai import analyze_resume

import PyPDF2
import docx
import json
import traceback


app = Flask(__name__)

# Change this in production
app.secret_key = "your_secret_key"

# Create database tables
Base.metadata.create_all(bind=engine)


# Home page
@app.route("/")
def home():
    if "user_id" in session:
        return redirect("/dashboard")
    
    return render_template("landing.html")


# Signup
@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        db = SessionLocal()

        email = request.form["email"]
        password = request.form["password"]

        # Check if user already exists
        existing_user = (
            db.query(models.User)
            .filter_by(email=email)
            .first()
        )

        if existing_user:

            db.close()

            return "User already exists. Please log in."

        # Create new user
        new_user = models.User(
            email=email,
            password=password
        )

        db.add(new_user)
        db.commit()
        db.close()

        return redirect("/login")

    return render_template("signup.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        db = SessionLocal()

        email = request.form["email"]
        password = request.form["password"]

        # Check login credentials
        user = (
            db.query(models.User)
            .filter_by(
                email=email,
                password=password
            )
            .first()
        )

        db.close()

        if user:

            session["user_id"] = user.id

            return redirect("/dashboard")

        else:

            return "Invalid credentials. Please try again."

    return render_template("login.html")


# Dashboard
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":

        user_goal = request.form.get("user_goal")

        file = request.files.get("resume_file")

        resume_text = None

        try:

            # Check if file was uploaded
            if file and file.filename != "":

                # PDF file
                if file.filename.lower().endswith(".pdf"):

                    pdf_reader = PyPDF2.PdfReader(file)

                    resume_text = ""

                    for page in pdf_reader.pages:

                        resume_text += page.extract_text() or ""

                # DOCX file
                elif file.filename.lower().endswith(".docx"):

                    doc = docx.Document(file)

                    resume_text = "\n".join(
                        [para.text for para in doc.paragraphs]
                    )

                else:

                    return (
                        "Unsupported file format. "
                        "Please upload a PDF or DOCX file."
                    )

            # Analyze resume
            if resume_text and user_goal:

                result = analyze_resume(
                    resume_text,
                    user_goal
                )

                # Save report to database
                db = SessionLocal()

                new_report = models.Report(
                    user_id=session["user_id"],
                    resume_text=resume_text,
                    result=json.dumps(result)
                )

                db.add(new_report)
                db.commit()
                db.close()

        except Exception as e:

            traceback.print_exc()

            result = f"An error occurred: {str(e)}"

    return render_template(
        "dashboard.html",
        user=session["user_id"],
        result=result
    )


# History
@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect("/login")

    db = SessionLocal()

    user_id = session["user_id"]

    reports = (
        db.query(models.Report)
        .filter_by(user_id=user_id)
        .all()
    )

    db.close()

    parsed_reports = []

    for report in reports:

        parsed_reports.append({
            "id": report.id,
            "resume_text": report.resume_text,
            "result": (
                json.loads(report.result)
                if report.result
                else None
            )
        })

    return render_template(
        "history.html",
        reports=parsed_reports
    )


# Logout
@app.route("/logout")
def logout():

    session.pop("user_id", None)

    return redirect("/login")


# Run Flask application
if __name__ == "__main__":

    app.run(debug=True)