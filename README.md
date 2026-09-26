# CareerLens AI

CareerLens AI is a Flask-based web application that analyzes a resume based on the user's career goal.

The user can create an account, upload a resume in PDF or DOCX format, enter a target job role, and get feedback from an AI model. The application also saves previous analyses so they can be viewed later.

This project was developed as part of the GIST Internship Python Development track, Task 4.

## What the project does

- User signup and login
- Upload resumes in PDF and DOCX format
- Enter a target job role or career goal
- Analyze the resume using an AI model
- Get a score, strengths, weaknesses and suggestions
- Save the analysis in the database
- View previous analyses from the History page

## Technologies used

- Python
- Flask
- SQLAlchemy
- TiDB Cloud (MySQL compatible)
- OpenRouter API
- PyPDF2
- python-docx
- HTML
- CSS
- Jinja2
- python-dotenv

## Project structure

```text
careerlens-ai/
│
├── app.py
├── ai.py
├── db.py
├── models.py
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
├── .gitignore
└── requirements.txt
````

## How to run

### 1. Clone the repository

```bash
git clone https://github.com/SyedaJuveriya/careerlens-ai.git
cd careerlens-ai
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file in the project folder:

```env
OPENROUTER_API_KEY=your_api_key
DATABASE_URL=your_database_url
```

The `.env` file should not be uploaded to GitHub.

### 5. Run the application

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## How to use

1. Create an account.
2. Log in.
3. Upload your resume.
4. Enter the job role or career goal you are targeting.
5. Submit the resume for analysis.
6. Check the feedback on the dashboard.
7. Open the History page to see previous analyses.

## Database

The project uses TiDB Cloud as the database. SQLAlchemy is used to connect the Flask application with the database.

Two main tables are used:

* `users` - stores user account details
* `reports` - stores resume analysis results

## Notes

API keys and database credentials are stored in environment variables instead of being written directly in the Python files.

For a production version, password hashing and other security improvements would be added.

## Live Link

🔗: [careerlens-ai-ffda.onrender.com](https://careerlens-ai-ffda.onrender.com/dashboard)

## Author

Syeda Juveriya



