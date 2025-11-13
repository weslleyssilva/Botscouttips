import time
import logging
from odds_monitor import check_odds
from telegram_utils import send_message

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    while True:
        try:
            message = check_odds()
            if message:
                send_message(message)
        except Exception as e:
            logging.error(f"Erro no loop principal: {e}")
        time.sleep(30)
