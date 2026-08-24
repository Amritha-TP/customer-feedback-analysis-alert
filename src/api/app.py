from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import os

from src.data.preprocess import clean_text
from src.alerts.telegram_alert import send_negative_alert


app = FastAPI(
    title="Customer Feedback Analyzer"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Load ML Model and Vectorizer
# --------------------------------------------------

model = joblib.load(
    "models/sentiment_model.pkl"
)

vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)


# --------------------------------------------------
# Request Model
# --------------------------------------------------

class Review(BaseModel):
    text: str


# --------------------------------------------------
# Serve Frontend
# --------------------------------------------------

frontend_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../frontend"
    )
)

app.mount(
    "/static",
    StaticFiles(directory=frontend_path),
    name="static"
)


@app.get("/")
def home():

    return FileResponse(
        os.path.join(
            frontend_path,
            "index.html"
        )
    )


# --------------------------------------------------
# Prediction API
# --------------------------------------------------

@app.post("/predict")
def predict(review: Review):

    # Clean text
    cleaned_text = clean_text(
        review.text
    )

    # TF-IDF transformation
    X = vectorizer.transform(
        [cleaned_text]
    )

    # Prediction
    sentiment = model.predict(X)[0]

    sentiment = str(sentiment).lower()

    # Telegram status
    telegram_alert_sent = False

    if sentiment == "negative":

        try:

            send_negative_alert(
                review.text
            )

            telegram_alert_sent = True

        except Exception as e:

            print(
                f"Telegram alert failed: {e}"
            )

    return {
        "sentiment": sentiment,
        "telegram_alert_sent": telegram_alert_sent
    }