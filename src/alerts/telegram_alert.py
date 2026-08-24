import os
import logging

import requests

logger = logging.getLogger(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage" if TOKEN else None


def telegram_configured() -> bool:
    return bool(TOKEN and CHAT_ID)


def send_negative_alert(review: str) -> bool:
    if not telegram_configured():
        logger.warning("TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set; skipping alert.")
        return False

    message = f"NEGATIVE REVIEW ALERT\n\n{review}"
    payload = {"chat_id": CHAT_ID, "text": message}

    try:
        response = requests.post(API_URL, data=payload, timeout=10)
        response.raise_for_status()
        return True
    except requests.RequestException as exc:
        logger.warning("Failed to send Telegram alert: %s", exc)
        return False