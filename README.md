# Sentiment_analyzer
📊 Sentiment Analyzer with AWS Comprehend
A lightweight web application that analyzes the sentiment of user-inputted text using Amazon Comprehend. It features a Python backend and a simple HTML frontend.

🚀 Features
🔍 Detect sentiment using AWS Comprehend (Positive, Negative, Neutral, Mixed)

🧠 Real-time input from HTML frontend

⚙️ Lightweight Python backend (FastAPI/Flask)

☁️ Secure use of AWS credentials via .env file

🧱 Tech Stack
Frontend: HTML, CSS, JavaScript (vanilla)

Backend: Python (boto3, FastAPI or Flask)

Cloud NLP: AWS Comprehend

🗂️ Project Structure
bash
Copy
Edit
sentiment-analyzer/
│
├── app.py               # Python backend (FastAPI/Flask)
├── templates/
│   └── index.html       # Frontend form
├── static/              # Optional CSS/JS files
├── .env                 # AWS credentials and config (not tracked in Git)
├── .gitignore
└── README.md
🔐 .env Setup
Create a .env file in the root directory:

env
Copy
Edit
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
✅ Don't worry, this file is already ignored in .gitignore.

📦 Install Requirements
bash
Copy
Edit
pip install boto3 python-dotenv fastapi uvicorn
(Or replace fastapi and uvicorn with flask if you're using Flask.)

▶️ Run the App
For FastAPI:

bash
Copy
Edit
uvicorn app:app --reload
For Flask:

bash
Copy
Edit
python app.py
Then visit: http://localhost:8000

💻 index.html Sample
Place in templates/index.html:

html
Copy
Edit
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Sentiment Analyzer</title>
</head>
<body>
  <h1>Enter text to analyze sentiment</h1>
  <form method="POST" action="/analyze">
    <textarea name="text" rows="5" cols="50"></textarea><br>
    <button type="submit">Analyze</button>
  </form>
</body>
</html>
