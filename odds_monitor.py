import os
import requests
from dotenv import load_dotenv

load_dotenv()

THE_ODDS_API_KEY = os.getenv("THE_ODDS_API_KEY")
SPORT_KEY = os.getenv("SPORT_KEY")
DIFFERENCE_THRESHOLD_PCT = float(os.getenv("DIFFERENCE_THRESHOLD_PCT", "5.0"))

def check_odds():
    url = f"https://api.the-odds-api.com/v4/sports/{SPORT_KEY}/odds"
    params = {
        "apiKey": THE_ODDS_API_KEY,
        "regions": "eu",
        "markets": "h2h",
        "oddsFormat": "decimal"
    }

    response = requests.get(url, params=params)
    data = response.json()

    for event in data:
        home = event["bookmakers"][0]["markets"][0]["outcomes"][0]
        away = event["bookmakers"][0]["markets"][0]["outcomes"][1]

        diff = abs(float(home["price"]) - float(away["price"]))
        if diff > DIFFERENCE_THRESHOLD_PCT / 100:
            return f"⚠️ Odd desajustada: {event['home_team']} x {event['away_team']}\n"                    f"{home['name']}: {home['price']} | {away['name']}: {away['price']}"
    return None
