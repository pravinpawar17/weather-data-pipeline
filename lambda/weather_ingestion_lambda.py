import json
import boto3
import requests
import os
from datetime import datetime

# Initialize S3 client
s3 = boto3.client("s3")

# Config
BUCKET = "weather-live-project"
CITIES = ["Mumbai", "Pune", "Nagpur", "Aurangabad", "Jalna"]
API_KEY = os.environ["OPENWEATHER_API_KEY"]

def lambda_handler(event, context):
    print("Weather Lambda started")

    for city in CITIES:
        try:
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            s3_key = f"raw/{city}/{datetime.utcnow().date()}.json"

            s3.put_object(
                Bucket=BUCKET,
                Key=s3_key,
                Body=json.dumps(data),
                ContentType="application/json"
            )

            print(f"Uploaded weather data for {city} to {s3_key}")

        except Exception as e:
            print(f"ERROR for city {city}: {str(e)}")

    return {
        "statusCode": 200,
        "body": "Weather data uploaded successfully"
    }
