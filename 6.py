import requests
from selenium import webdriver
import time,datetime,pytz
from prettytable import PrettyTable
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from telethon import TelegramClient,events

# bot_token="6680273534:AAF1R3ieOUC4SdTog-hmFfT8f38VH8UY5Cs"
# chat_id="-1002034419658"
# api_id="1082319"
# api_hash="c778e52f3aa8904729c37d8723fc85e4"
#
# result_table=PrettyTable(["Currency","Sell","Buy"])
# gold_table=PrettyTable(["Gold Coin", "Sell", "Buy"])
# start_time = time.time()
# url = 'https://www.bonbast.com/'
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(service=ChromeService(), options=options)
#
# # Load the webpage
# driver.get(url)
# time_extracted = datetime.datetime.now(pytz.timezone('Asia/Tehran'))
# print(f"Time in IRST format when data is extracted: {time_extracted.strftime('%Y-%m-%d %H:%M:%S')}")
# # Wait for a few seconds to ensure JavaScript has loaded
# # driver.implicitly_wait(5)
#
# # Get the page source after JavaScript execution
# page_source = driver.page_source
#
# # Close the browser
# driver.quit()
#
# with open('./source.html', 'w') as f:
#   f.write(page_source)

f = open('source.html', 'r')
contents=f.read()
f.close()
# Parse the page source with BeautifulSoup
soup = BeautifulSoup(contents, 'html.parser')

currency_table = soup.find_all('table', class_='table-condensed')
max_length=0
max_name=''

# ... (previous code)

title = "+-------------------------+--------------+--------------+\n"
header = "|     Currency            |     Sell     |      Buy     |\n"
separator = "+-------------------------+--------------+--------------+\n"
test_table = title + header + separator

for table in currency_table:
    rows = table.find_all('tr')
# Find the maximum length of currency names
max_currency_length = max(len(columns[1].text.strip()) for row in rows for columns in row.find_all('td'))

for table in currency_table:
    rows = table.find_all('tr')
    round_count = 1  # without this, the code runs 15 times IDK why
    for row in rows:
        if round_count == 2:
            break

        for row in rows:
            columns = row.find_all('td')
            if columns[0].text.strip() == 'Code':
                round_count += 1
                continue
            code = columns[0].text.strip()
            currency = columns[1].text.strip()
            sell_price = columns[2].text.strip()
            buy_price = columns[3].text.strip()

            # Calculate the padding based on the maximum currency length
            currency_pad = " " * (max_currency_length - len(currency) + 4)
            sell_pad = " " * (14 - len(sell_price))
            buy_pad = " " * (14 - len(buy_price))

            # Using format method for string formatting
            aligned_row = f"|{currency}{currency_pad}|{sell_price}{sell_pad}|{buy_price}{buy_pad}|\n"

            test_table += aligned_row

# Now send test_table to your Telegram channel
# ...

# Add a closing line to complete the ASCII table
test_table += "+-------------------------+--------------+--------------+"


print(test_table)
bot_token="6680273534:AAF1R3ieOUC4SdTog-hmFfT8f38VH8UY5Cs"
chat_id="-1002034419658"
api_id="1082319"
api_hash="c778e52f3aa8904729c37d8723fc85e4"
markdown_table =f"```\n{test_table}```"
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

params = {
    "chat_id": chat_id,
    "text": markdown_table,
    "parse_mode": "markdown"
}

response = requests.post(url, params=params)