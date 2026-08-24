# Customer Feedback Analyzer

An end-to-end **NLP sentiment analysis application** that analyzes customer feedback using a machine learning model and automatically sends a **Telegram alert when negative feedback is detected**.

The project combines traditional NLP, machine learning, FastAPI, and an interactive web interface into a complete real-time feedback analysis application.

---

## 🚀 Project Overview

Customer feedback can contain valuable information about customer satisfaction, product quality, and potential issues.

This application allows a user to enter customer feedback through an interactive web interface. The application then:

1. Cleans and preprocesses the text.
2. Converts the text into numerical features using **TF-IDF**.
3. Uses a trained machine learning model to predict sentiment.
4. Displays the prediction through the web interface.
5. Automatically sends a **Telegram notification** when negative feedback is detected.

### Application Flow

```text
Customer Feedback
        ↓
Interactive Web UI
        ↓
FastAPI /predict
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Machine Learning Model
        ↓
Sentiment Prediction
        ↓
 ┌───────────────┐
 │ Positive      │
 │ Neutral       │
 │ Negative      │
 └───────┬───────┘
         │
         ▼
Negative Feedback
         │
         ▼
Telegram Alert
```

---

## ✨ Features

* Customer feedback text input
* Interactive web interface
* NLP text preprocessing
* TF-IDF feature extraction
* Machine learning sentiment classification
* Positive, neutral, and negative sentiment detection
* FastAPI REST API
* Real-time prediction
* Automated Telegram alerts for negative feedback
* Swagger API documentation
* Environment-based Telegram credential management

---

## 🛠️ Technology Stack

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Application and ML development |
| Scikit-learn     | Machine learning and TF-IDF    |
| Pandas           | Data processing                |
| NumPy            | Numerical operations           |
| Joblib           | Model serialization            |
| FastAPI          | REST API                       |
| Uvicorn          | Application server             |
| HTML/CSS         | Web interface                  |
| JavaScript       | Frontend interaction           |
| Telegram Bot API | Negative feedback alerts       |
| Git/GitHub       | Version control                |

---

## 📂 Project Structure

```text
customer_feedback_analysis/
│
├── .venv/                     # Virtual environment
│
├── data/                      # Data storage
│   ├── processed/             # Cleaned and preprocessed data
│   ├── raw/                   # Raw input data
│   └── sample/                # Sample datasets for testing
│
├── frontend/                  # Frontend interface
│   ├── index.html             # Web UI for customer feedback input
│   └── script.js              # Client‑side logic and API calls
│
├── models/                    # Machine learning models
│   ├── sentiment_model.pkl    # Trained sentiment analysis model
│   └── tfidf_vectorizer.pkl   # TF‑IDF vectorizer for text features
│
├── notebooks/                 # Jupyter notebooks for experimentation
│
├── src/                       # Backend source code
│   ├── alerts/                # Telegram notification logic
│   ├── api/                   # REST API endpoints
│   ├── data/                  # Data loading and preprocessing utilities
│   ├── features/              # Feature extraction and transformation
│   ├── models/                # Model loading and inference
│   └── utils/                 # Helper functions and common utilities
│
├── main.py                    # Entry point for running the webapp
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore configuration
```

---

## 🧠 Machine Learning Pipeline

The application follows a traditional NLP machine learning pipeline:

```text
Raw Customer Feedback
        ↓
Text Cleaning
        ↓
TF-IDF Vectorization
        ↓
Trained ML Model
        ↓
Sentiment Prediction
```

### Text Preprocessing

The preprocessing stage prepares raw customer feedback for machine learning by cleaning and normalizing the text.

### TF-IDF

TF-IDF converts the processed text into numerical feature vectors that can be consumed by the machine learning model.

### Sentiment Classification

The trained model predicts one of the supported sentiment classes:

```text
Positive
Neutral
Negative
```

---

## 🔔 Telegram Alert System

Negative customer feedback triggers an automated Telegram notification.

```text
Sentiment = Negative
        ↓
send_negative_alert()
        ↓
Telegram Bot API
        ↓
Business Owner Notification
```

This provides a simple real-time mechanism for businesses to identify potentially problematic customer experiences.

---

## 🔐 Environment Variables

Telegram credentials are **not stored in the source code**.

The application reads them using environment variables:

```python
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
```

### Windows

Set the variables using PowerShell:

```powershell
setx TELEGRAM_BOT_TOKEN "your_bot_token"
setx TELEGRAM_CHAT_ID "your_chat_id"
```

Restart your terminal after using `setx`.

**Never commit your Telegram bot token or chat ID to GitHub.**

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Amritha-TP/customer-feedback-analysis-alert.git

```

### 2. Navigate to the project

```bash
cd customer-feedback-analysis
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

### 4. Activate the environment

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server from the project root:

```powershell
uvicorn src.api.app:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Open the URL in your browser to access the interactive Customer Feedback Analyzer.

---

## 📡 API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

### Prediction Endpoint

```text
POST /predict
```

### Request

```json
{
  "text": "The product quality is terrible and I am very disappointed."
}
```

### Response

```json
{
  "sentiment": "negative",
  "telegram_alert_sent": true
}
```

For positive feedback:

```json
{
  "sentiment": "positive",
  "telegram_alert_sent": false
}
```

---

## 🖥️ Interactive Application

The application provides a simple interface where users can enter customer feedback and receive an immediate sentiment prediction.

Example:

```text
Customer Feedback:

"The product is excellent and I am very happy with my purchase."

                ↓

Sentiment: POSITIVE
```

Negative feedback triggers the Telegram notification workflow.

---

## 💼 Business Use Case

The application can be used by businesses to monitor customer feedback and identify negative experiences quickly.

Potential applications include:

* E-commerce reviews
* Product feedback
* Customer support feedback
* Service reviews
* Restaurant reviews
* Customer satisfaction monitoring
* Online review monitoring

Automated negative-feedback alerts can help businesses respond to customer issues faster.

---

## 🔮 Future Improvements

Potential enhancements include:

* Deploy the application to a cloud platform
* Add authentication
* Add sentiment confidence scores
* Store customer feedback in a database
* Add feedback analytics dashboards
* Track sentiment trends over time
* Add batch CSV sentiment analysis
* Add model performance monitoring
* Add Docker deployment
* Add CI/CD pipeline
* Add more advanced NLP models such as BERT

---

## 📌 Skills Demonstrated

This project demonstrates hands-on experience with:

* Natural Language Processing
* Text preprocessing
* TF-IDF vectorization
* Traditional machine learning
* Model inference
* Python
* Scikit-learn
* FastAPI
* REST APIs
* Frontend and backend integration
* Environment variable management
* Telegram API integration
* Git and GitHub
* End-to-end ML application development

---

## 👩‍💻 Author

**Amritha Ponram**

Machine Learning Engineer | NLP | Computer Vision | Predictive Modeling | Python

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
