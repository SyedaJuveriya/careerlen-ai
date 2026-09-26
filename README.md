# CareerLens AI 🔍

**CareerLens AI** is an AI-powered resume analyzer web application that helps job seekers understand how well their resume aligns with a specific job goal. Users can sign up, upload their resume (PDF/DOCX), enter their target role or job description, and receive an instant AI-generated analysis — including a match score, strengths, weaknesses, and actionable suggestions for improvement.

Built as part of the GIST Internship Python Development track (Task 4 — Advanced+: Python-Based Real-World Application), this project demonstrates AI integration, database persistence, REST API consumption, and a structured Flask project architecture.

---

## ✨ Features

- 🔐 **User Authentication** — Secure signup/login system with session-based access control
- 📄 **Resume Parsing** — Supports both PDF and DOCX resume uploads
- 🤖 **AI-Powered Analysis** — Uses an LLM (via OpenRouter API) to evaluate resumes against a user-defined job goal
- 📊 **Structured Feedback** — Returns a score out of 100, along with strengths, weaknesses, and improvement suggestions
- 🕘 **Analysis History** — Every report is saved to the database and viewable later on the History page
- 🎨 **Clean, Responsive UI** — Custom-styled interface built with Jinja2 templates and CSS

---

## 🛠️ Tech Stack

| Layer          | Technology                          |
|----------------|--------------------------------------|
| Backend        | Python, Flask                        |
| Database       | MySQL (TiDB Cloud) via SQLAlchemy    |
| AI Integration | OpenRouter API (OpenAI-compatible SDK) |
| File Parsing   | PyPDF2, python-docx                  |
| Frontend       | HTML, CSS, Jinja2 Templates          |
| Environment    | python-dotenv for config management  |

---

## 📁 Project Structure

```
careerlens-ai/
├── app.py                 # Flask routes and core application logic
├── ai.py                  # AI resume analysis logic (OpenRouter integration)
├── db.py                  # Database engine and session configuration
├── models.py               # SQLAlchemy models (User, Report)
├── static/
│   └── style.css           # Application styling
├── templates/
│   ├── base.html            # Base layout with navigation
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html       # Resume upload + analysis results
│   └── history.html         # Past analysis reports
├── .env                    # Environment variables (not committed)
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/SyedaJuveriya/careerlen-ai.git
cd careerlens-ai
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Get a free API key from [OpenRouter](https://openrouter.ai/keys) — no card required.

### 5. Set up the database
Update the `DATABASE_URL` in `db.py` with your own MySQL/TiDB connection string.

### 6. Run the application
```bash
python app.py
```
Visit **http://127.0.0.1:5000** in your browser.

---

## 🚀 Usage

1. **Sign up** for a new account
2. **Log in** with your credentials
3. On the **Dashboard**, upload your resume (PDF/DOCX) and enter your target job role or description
4. Click **Analyze Resume** to get instant AI feedback
5. View all past analyses on the **History** page

---

## 🔒 Security Notes

- API keys are managed via environment variables (`.env`) and never hardcoded
- Sensitive files (`venv/`, `__pycache__/`, `.env`) are excluded via `.gitignore`
- Passwords are stored per user account (recommended: hash passwords with `werkzeug.security` before production use)

---

## 📌 Future Improvements

- Password hashing for stronger security
- "Forgot Password" functionality
- Export analysis reports as PDF
- Support for more resume formats
- Deployment to a production hosting platform (Render/Railway)

---

## 👩‍💻 Author

**Syeda Juveriya**
Final-year B.Tech student, Artificial Intelligence & Data Science
GitHub: [@SyedaJuveriya](https://github.com/SyedaJuveriya)
