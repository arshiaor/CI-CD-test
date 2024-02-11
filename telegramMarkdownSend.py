from telethon import TelegramClient,events
import requests
bot_token="6680273534:AAF1R3ieOUC4SdTog-hmFfT8f38VH8UY5Cs"
chat_id="-1002034419658"
api_id="1082319"
api_hash="c778e52f3aa8904729c37d8723fc85e4"

result_table="""
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
"""

print(f'<pre>{result_table}</pre>')
markdown_table =f'<pre>{result_table}</pre>'
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

params = {
    "chat_id": chat_id,
    "text": markdown_table,
    "parse_mode": "html"
}

response = requests.post(url, params=params)