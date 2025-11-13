import time
import logging
from odds_monitor import check_odds
from telegram_utils import send_message

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # Mensagem de inicialização
    try:
        send_message("✅ Bot conectado com sucesso!\\nMonitorando odds em tempo real...")
        logging.info("Mensagem de teste enviada ao Telegram.")
    except Exception as e:
        logging.error(f"Falha ao enviar mensagem de teste: {e}")

    # Loop principal
    while True:
        try:
            message = check_odds()
            if message:
                send_message(message)
        except Exception as e:
            logging.error(f"Erro no loop principal: {e}")
        time.sleep(30)
