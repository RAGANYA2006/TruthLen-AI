# 🔍 TruthLens AI — Fake News Detection System

TruthLens AI is an AI-powered web application designed to analyze news articles and predict whether the given content is **FAKE** or **REAL**.

The system uses **Natural Language Processing (NLP)** and **Machine Learning** to process news content. The text is converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)** and classified using a **Logistic Regression** model.

The application also stores analyzed news and prediction results in a **SQLite database** and provides an **Excel report** containing the analysis history.

---

## 🚀 Project Overview

The rapid spread of misleading information through websites and social media makes it difficult to distinguish between genuine and fake news.

TruthLens AI provides a simple interface where users can enter a news article or headline and receive an AI-based prediction.

### Users can:

- 📰 Enter a news article or headline
- 🤖 Analyze the content using Machine Learning
- 🔍 Predict whether the news is **FAKE** or **REAL**
- 📊 View the prediction confidence
- 💾 Store analysis results in SQLite
- 📜 View analysis history
- 📑 Generate an Excel analysis report

---

# ✨ Features

- 🤖 AI-powered fake news classification
- 📰 News article and headline analysis
- 🧠 Natural Language Processing
- 📌 TF-IDF feature extraction
- 📊 Logistic Regression classification
- 🎯 **98.95% test accuracy**
- 📈 Prediction confidence score
- 💾 SQLite database storage
- 📜 Analysis history
- 📑 Excel report generation
- ⚡ Flask REST API
- ⚛️ React frontend
- 🎨 Responsive user interface
- 🔄 Frontend-backend integration
- 🕒 Analysis date and time tracking

---

# 🧠 Machine Learning

TruthLens AI uses a supervised Machine Learning approach for fake news classification.

## Machine Learning Pipeline

```text
News Article / Headline
          ↓
     Text Cleaning
          ↓
    TF-IDF Vectorization
          ↓
   Logistic Regression
          ↓
     ┌────┴────┐
     ↓         ↓
   FAKE       REAL
     │         │
     └────┬────┘
          ↓
   Confidence Score
          ↓
    Store Analysis
          ↓
 SQLite + Excel Report
```

---

## 🔬 Algorithm Used

### Logistic Regression

Logistic Regression is used as the classification algorithm to determine whether the submitted news belongs to the **FAKE** or **REAL** category.

### TF-IDF

TF-IDF is used to convert text into numerical features that can be processed by the Machine Learning model.

TF-IDF considers the importance of words within a document and across the complete collection of documents.

---

# 📊 Dataset

The model was trained using a dataset containing separate fake and real news records.

| Category | Number of Records |
|----------|------------------:|
| Fake News | 23,481 |
| Real News | 21,417 |
| **Total** | **44,898** |

---

## 📚 Dataset Split

The dataset was divided into training and testing sets.

| Dataset | Records |
|---------|--------:|
| Training | 35,918 |
| Testing | 8,980 |
| **Total** | **44,898** |

The dataset itself is not included in the GitHub repository because of its large file size.

---

# 🎯 Model Performance

The trained Logistic Regression model achieved:

## **98.95% Accuracy**

### Classification Report

| Class | Precision | Recall | F1-Score |
|-------|----------:|-------:|---------:|
| FAKE | 0.99 | 0.99 | 0.99 |
| REAL | 0.99 | 0.99 | 0.99 |

### Overall Accuracy

```text
Accuracy: 98.95%
```

The model was evaluated using **8,980 testing records**.

---

# 🛠️ Technologies Used

## Frontend

- React
- Vite
- JavaScript
- HTML5
- CSS3
- Lucide React

## Backend

- Python
- Flask
- Flask-CORS

## Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib
- TF-IDF
- Logistic Regression

## Database

- SQLite

## Reporting

- OpenPyXL
- Microsoft Excel

## Development Tools

- Visual Studio Code
- Git
- GitHub
- PowerShell

---

# 📁 Project Structure

```text
TruthLen-AI/
│
├── BACKEND/
│   ├── app.py
│   ├── database.py
│   ├── export_excel.py
│   ├── train_model.py
│   ├── fake_news_model.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── fake_news.db
│   └── analysis_reports.xlsx
│
├── DATASET/
│   ├── Fake.csv
│   └── True.csv
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── NOTEBOOK/
│
├── screenshots/
│
├── .gitignore
│
└── README.md
```

> Generated model, database, Excel, and dataset files may be excluded from the GitHub repository using `.gitignore`.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/RAGANYA2006/TruthLen-AI.git
```

Navigate to the project:

```bash
cd TruthLen-AI
```

---

# 🐍 Backend Setup

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 📦 Install Python Dependencies

Run:

```powershell
pip install flask flask-cors scikit-learn pandas numpy joblib openpyxl
```

---

# 🗃️ Dataset Setup

Place the dataset files inside:

```text
DATASET/
```

The expected files are:

```text
DATASET/
├── Fake.csv
└── True.csv
```

The dataset contains:

- Fake news records
- Real news records

The dataset is used only for model training.

---

# 🧠 Train the Machine Learning Model

Navigate to the backend:

```powershell
cd BACKEND
```

Run:

```powershell
python train_model.py
```

The training process performs:

```text
Load Dataset
     ↓
Combine Fake + Real News
     ↓
Clean Text
     ↓
Split Dataset
     ↓
Create TF-IDF Features
     ↓
Train Logistic Regression
     ↓
Evaluate Model
     ↓
Save Model
```

After successful training, the following files are created:

```text
fake_news_model.pkl
tfidf_vectorizer.pkl
```

---

# ▶️ Run the Flask Backend

From the `BACKEND` directory:

```powershell
python app.py
```

The Flask server runs at:

```text
http://127.0.0.1:5000
```

Expected terminal output:

```text
Serving Flask app 'app'
Debug mode: on
Running on http://127.0.0.1:5000
```

---

# ⚛️ Frontend Setup

Open a **new terminal** while the Flask server is running.

Navigate to the frontend:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

If Lucide React is required:

```powershell
npm install lucide-react
```

---

# ▶️ Run the React Frontend

Start the Vite development server:

```powershell
npm run dev
```

Vite will provide a local URL similar to:

```text
http://localhost:5173
```

Open the URL in your browser.

---

# 🔄 Application Workflow

```text
                    USER
                      │
                      ↓
               React Frontend
                      │
                      ↓
            News Article / Headline
                      │
                      ↓
                Flask REST API
                      │
                      ↓
                Text Cleaning
                      │
                      ↓
              TF-IDF Vectorizer
                      │
                      ↓
            Logistic Regression
                      │
                ┌─────┴─────┐
                ↓           ↓
              FAKE         REAL
                │           │
                └─────┬─────┘
                      ↓
               Confidence Score
                      │
             ┌────────┴────────┐
             ↓                 ↓
       SQLite Database     Excel Report
```

---

# 📡 API

TruthLens AI uses a Flask REST API to connect the React frontend with the Machine Learning model.

## Health Check

### Endpoint

```text
GET /
```

### URL

```text
http://127.0.0.1:5000/
```

---

## 🔍 Analyze News

### Endpoint

```text
POST /predict
```

### Request

```json
{
  "text": "Your news article or headline here"
}
```

### Example Response

```json
{
  "prediction": "FAKE",
  "confidence": 89.3,
  "message": "News analyzed successfully"
}
```

The prediction can be:

```text
FAKE
```

or:

```text
REAL
```

---

# 📜 Analysis History

TruthLens AI stores analyzed news in a SQLite database.

### Endpoint

```text
GET /history
```

The endpoint retrieves previously stored analysis records.

Example:

```json
{
  "success": true,
  "count": 6,
  "analyses": []
}
```

The actual analysis records are stored in the database.

---

# 💾 SQLite Database

Database file:

```text
BACKEND/fake_news.db
```

The database stores information such as:

| Field | Description |
|-------|-------------|
| ID | Unique analysis ID |
| News Text | Submitted article or headline |
| Prediction | FAKE or REAL |
| Confidence | Model confidence |
| Analyzed At | Date and time of analysis |

Example:

```text
ID: 6
Prediction: FAKE
Confidence: 89.30%
Analyzed At: 2026-08-13
```

---

# 📑 Excel Analysis Report

TruthLens AI can export stored analysis records to an Excel file.

Generated file:

```text
BACKEND/analysis_reports.xlsx
```

The Excel report can contain:

| ID | News Text | Prediction | Confidence | Analyzed At |
|----|-----------|------------|------------|-------------|
| 1 | News Article 1 | REAL | 94.25% | 2026-08-13 |
| 2 | News Article 2 | FAKE | 89.30% | 2026-08-13 |
| 3 | News Article 3 | REAL | 91.80% | 2026-08-13 |

The Excel report is generated using **OpenPyXL**.

---

# 📊 Example Analysis

### Input

```text
Scientists announce a major breakthrough that will completely
eliminate all diseases within the next few weeks.
```

### Example Result

```text
Analysis Result

Prediction: FAKE

Confidence: 89.30%

News analyzed successfully
```

> The example result is only for demonstration. Actual predictions depend on the trained Machine Learning model.

---

# 🖥️ Application Features

## 🏠 Home

Provides an introduction to the TruthLens AI system.

## 📰 News Input

Users can enter:

- News headlines
- News articles
- News content

## 🤖 AI Analysis

The submitted text is processed by the Machine Learning model.

## 🔍 Prediction

The system predicts:

```text
FAKE
```

or

```text
REAL
```

## 📈 Confidence

The application displays the model's prediction confidence.

## 💾 Database

The analysis result is stored in SQLite.

## 📑 Excel Report

Stored results can be exported into an Excel file.

---

# 📸 Screenshots

Project screenshots are stored in:

```text
screenshots/
```

You can display them in this README using:

```markdown
![TruthLens AI Home Page](screenshots/home.png)
```

```markdown
![News Analyzer](screenshots/analyzer.png)
```

```markdown
![Analysis Result](screenshots/result.png)
```

---

# 🔐 GitHub Files and Security

The following files should not normally be uploaded to GitHub:

```text
venv/
.venv/
__pycache__/
*.pyc
.env
.vscode/
node_modules/
frontend/node_modules/
frontend/dist/
DATASET/
```

Generated files can also be excluded when appropriate:

```text
*.db
*.xlsx
*.pkl
```

The `.gitignore` file is used to prevent unnecessary or sensitive files from being committed.

---

# ⚠️ Disclaimer

TruthLens AI is a **Machine Learning-based classification system**.

A prediction such as:

```text
Prediction: FAKE
Confidence: 89.30%
```

does not guarantee that the information is objectively false.

The confidence value represents the model's confidence in its classification based on patterns learned from the training data.

Important information should always be verified using trusted and reliable sources.

---

# 🔮 Future Enhancements

Future versions of TruthLens AI may include:

- 🌐 Real-time news verification
- 🔗 News URL analysis
- 🔎 Source credibility verification
- 📰 Real-time news API integration
- 📊 Interactive analytics dashboard
- 🧠 Transformer-based NLP models
- 🤖 Deep Learning-based classification
- 👤 User authentication
- 📄 PDF report generation
- 🔍 Search and filter analysis history
- 📈 Prediction statistics
- ☁️ Cloud deployment
- 📱 Improved mobile responsiveness
- 🌍 Multi-language fake news detection

---

# 🎯 Project Objectives

The main objectives of TruthLens AI are:

1. Detect potentially fake news using Machine Learning.
2. Apply Natural Language Processing to news content.
3. Build a complete Machine Learning-powered web application.
4. Provide prediction confidence scores.
5. Store analysis history using SQLite.
6. Generate Excel analysis reports.
7. Develop a React-based frontend.
8. Build a Flask REST API backend.
9. Integrate frontend and backend.
10. Provide a simple and user-friendly interface.

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Natural Language Processing
- Text preprocessing
- TF-IDF
- Logistic Regression
- Machine Learning classification
- Model evaluation
- Flask REST API
- React
- Vite
- SQLite
- OpenPyXL
- Excel reporting
- REST API communication
- Frontend-backend integration
- Git
- GitHub

---

# 📈 Training Output

The model training process produced the following results:

```text
Loading datasets...
Fake news records: 23481
Real news records: 21417
Total records: 44898

Cleaning text...

Training records: 35918
Testing records: 8980

Creating TF-IDF features...

Training Logistic Regression model...

Accuracy: 98.95%
```

### Saved Model Files

```text
fake_news_model.pkl
tfidf_vectorizer.pkl
```

---

# 🏆 Project Highlights

| Component | Technology |
|-----------|------------|
| Frontend | React + Vite |
| Backend | Flask |
| NLP | TF-IDF |
| ML Algorithm | Logistic Regression |
| Accuracy | 98.95% |
| Database | SQLite |
| Reporting | Excel / OpenPyXL |
| API | Flask REST API |
| Version Control | Git + GitHub |

---

# 👩‍💻 Author

## Raganya N

**B.E. Computer Science and Engineering**

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Data Science
- Python
- Java
- Web Development

---

# ⭐ Acknowledgements

TruthLens AI was developed as an academic and portfolio project demonstrating the integration of:

```text
Machine Learning
       +
Natural Language Processing
       +
React
       +
Flask
       +
SQLite
       +
Excel Reporting
```

---

# 📄 License

This project is intended for **educational, academic, and portfolio purposes**.

---

# 🔗 GitHub Repository

**TruthLens AI**

https://github.com/RAGANYA2006/TruthLen-AI

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
