import requests
from selenium import webdriver
import time,datetime,pytz
from prettytable import PrettyTable
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from telethon import TelegramClient,events

bot_token="6680273534:AAF1R3ieOUC4SdTog-hmFfT8f38VH8UY5Cs"
chat_id="-1002034419658"
api_id="1082319"
api_hash="c778e52f3aa8904729c37d8723fc85e4"

result_table=PrettyTable(["Currency","Sell","Buy"])
gold_table=PrettyTable(["Gold Coin", "Sell", "Buy"])
start_time = time.time()
url = 'https://www.bonbast.com/'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService(), options=options)

# Load the webpage
driver.get(url)
time_extracted = datetime.datetime.now(pytz.timezone('Asia/Tehran'))
print(f"Time in IRST format when data is extracted: {time_extracted.strftime('%Y-%m-%d %H:%M:%S')}")
# Wait for a few seconds to ensure JavaScript has loaded
# driver.implicitly_wait(5)

# Get the page source after JavaScript execution
page_source = driver.page_source

# Close the browser
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

currency_table = soup.find_all('table', class_='table-condensed')
max_length=0
max_name=''

for table in currency_table:
    rows = table.find_all('tr')
    round_count=1 #without this , the code runs 15 times idk why
    for row in rows:
        if round_count==2:
            break
        # Adjust the CSS selector to target the specific 'td' with an id

        for row in rows:
            columns = row.find_all('td')
            if columns[0].text.strip() == 'Code':
                round_count+=1
                continue
            code = columns[0].text.strip()
            currency = columns[1].text.strip()
            sell_price = columns[2].text.strip()
            buy_price = columns[3].text.strip()
            result_table.add_row([currency,sell_price,buy_price])
            # print(f"Code: {code}, Currency: {currency}, Sell: {sell_price}, Buy: {buy_price}")

test_table=''
title="     Currency     "+""*4 + "   sell   " + ""*4 + "   Buy   "+""*4


# def find_gold_table(soup):
#     # Look for all tables within the specified div
#     gold_tables = soup.find('div', class_='col-xs-12 col-lg-6').find('table', class_='table')
#
#     for table in gold_tables:
#         # Find all rows in the table
#         rows = table.find_all('tr')
#
#         # Check if the table has at least one row
#         if rows[0].text.strip() == 'Gold Coins':
#             # Check if all rows in the table have exactly three items
#             if all(len(row.find_all('td')) == 3 for row in rows):
#                 return table  # Return the table if it meets the criteria
#
#     return None  # Return None if no suitable table is found
#
# # Example usage:
# gold_table_data = find_gold_table(soup)
#
# # Proceed with extracting and displaying gold coin information if gold_table_data is not None
# if gold_table_data:
#     for row_data in gold_table_data.find_all('tr'):
#         columns = row_data.find_all('td')
#
#         gold_coin = columns[0].text.strip()
#         sell_price = columns[1].text.strip()
#         buy_price = columns[2].text.strip()
#         gold_table.add_row([gold_coin, sell_price, buy_price])
# else:
#     print("Gold table not found.")
#
# #
# print(gold_table)

# print(result_table)
# markdown_table = "```" + str(result_table) + "```"
# url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
#
# params = {
#     "chat_id": chat_id,
#     "text": markdown_table,
#     "parse_mode": "markdown"
# }
#
# response = requests.post(url, params=params)





end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

# Print elapsed time in hours, minutes, and seconds
elapsed_hours, elapsed_remainder = divmod(elapsed_time, 3600)
elapsed_minutes, elapsed_seconds = divmod(elapsed_remainder, 60)

print(f"Script execution time: {int(elapsed_hours)}h {int(elapsed_minutes)}m {int(elapsed_seconds)}s")