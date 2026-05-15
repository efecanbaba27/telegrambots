import requests
import time
import random

TOKEN = "8832387488:AAEQH7za105IXhHWNxpGdYWif7pT1qSBf_s"
CHAT_ID = "-1003948726380"

mesajlar = [
    "SEEAAAXDDD.?",
    "ASSEEEXDDD.?",
    "SEEAAAXDDD.?",
    "ASSEEEXDDD.?"
]

while True:
    mesaj = random.choice(mesajlar)

    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": mesaj
        }
    )

    time.sleep(60)
