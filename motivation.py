import requests
import random

TOKEN = "8982228087:AAH4DSJ9nRhc0KIYNgcAcfV3nGA_ezO3TbE"
CHAT_ID = "8713385516"

MOTIVATION_MESSAGE_LIST = [
    "⭐️ English: Every day is a new beginning.\n🇲🇲 မြန်မာ: ရက်တိုင်းဟာ အစသစ်တစ်ခုပါပဲ။",
    "⭐️ English: Small daily improvements lead to stunning results.\n🇲🇲 မြန်မာ: နေ့စဉ်တိုးတက်မှုက အံ့မခန်းရလဒ်ကို ဖန်တီးပေးတယ်။",
    "⭐️ English: Believe you can and you're halfway there.\n🇲🇲 မြန်မာ: လုပ်နိုင်တယ်လို့ ယုံကြည်လိုက်ပါ။",
    "⭐️ English: Push yourself, because no one else will.\n🇲🇲 မြန်မာ: ကိုယ့်ကိုကိုယ် တွန်းအားယူပါ။",
    "⭐️ English: Success doesn't just find you; you must go get it.\n🇲🇲 မြန်မာ: အောင်မြင်မှုကို ကိုယ်တိုင် သွားယူရပါမယ်။"
]

def send_telegram_message():
    message = random.choice(MOTIVATION_MESSAGE_LIST)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("မက်ဆေ့ချ် အောင်မြင်စွာ ပို့ပြီးပါပြီ။")
        else:
            print("ပို့၍ မအောင်မြင်ပါ၊", response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    send_telegram_message()
