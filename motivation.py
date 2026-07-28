import os
import requests

# GitHub Secrets (သို့မဟုတ်) Environment Variables ထဲကနေ လှမ်းယူခြင်း
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = "မင်္ဂလာပါ! နေ့စဉ်အားပေးစကား..."
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

response = requests.get(url)
print(response.json())
