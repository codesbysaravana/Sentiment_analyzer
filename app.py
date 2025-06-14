from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Initialize AWS Comprehend client
comprehend = boto3.client(
    'comprehend',
    region_name=os.getenv("AWS_REGION")
)

@app.post("/sentiment")
async def detect_sentiment(request: Request):
    """
    Receives text, sends it to AWS Comprehend for sentiment analysis,
    and returns the sentiment and confidence scores.
    """
    try:
        data = await request.json()
        text = data.get("text")

        if not text:
            return {"error": "No text provided"}, 400

        # Call AWS Comprehend's detect_sentiment API, takes in text and language code 
        response = comprehend.detect_sentiment(
            Text=text,
            LanguageCode='en'  # 'en' for English. 
        )

        return {
            "sentiment": response["Sentiment"],
            "scores": response["SentimentScore"]
        }
    except Exception as e:
        return {"error": str(e)}, 500