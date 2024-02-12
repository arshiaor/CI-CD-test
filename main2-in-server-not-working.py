import requests,os
from selenium import webdriver
import time,datetime,pytz
from prettytable import PrettyTable
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService


# bot_token=os.environ["BOT_TOKEN"]
# chat_id=os.environ["CHAT_ID"]
# api_id=os.environ["API_ID"]
# api_hash=os.environ["API_HASH"]

bot_token="6680273534:AAF1R3ieOUC4SdTog-hmFfT8f38VH8UY5Cs"
chat_id="-1002034419658"
api_id="1082319"
api_hash="c778e52f3aa8904729c37d8723fc85e4"
while True:
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

    title="     Currency     "+" "*4 + "   sell   " + " "*4 + "   Buy   "+" "*4 +"\n"
    # dashes="-"*(len(title)-5) + "\n" for beauty
    test_table= title+"\n"

    for table in currency_table:
        rows = table.find_all('tr')
        round_count=1 #without this , the code runs 15 times idk why
        for row in rows:
            if round_count==2:
                break
            # Adjust the CSS selector to target the specific 'td' with an id

            for row2 in rows:
                columns = row2.find_all('td')
                if columns[0].text.strip() == 'Code':
                    round_count+=1
                    continue
                code = columns[0].text.strip()
                currency = columns[1].text.strip()
                sell_price = columns[2].text.strip()
                buy_price = columns[3].text.strip()
                test_table_rows=[]
                # currency = "  " + currency + "  "
                # sell_price = "    " + sell_price + "  "
                # buy_price = "    " + buy_price + "  "
                #
                # # Calculate padding needed to align columns
                # currency_pad = " " * (25 - len(currency))
                # sell_pad = " " * (6 - len(sell_price))
                # buy_pad = " " * (7 - len(buy_price))

                # Construct aligned row
                aligned_row = "{:<25} {:<10} {:<10}\n".format(currency, sell_price, buy_price)

                # Append to rows

                test_table_rows.append(aligned_row)
                test_table=test_table +"-"*(len(title)-5) + "\n" + "\n".join(test_table_rows)
                # result_table.add_row([currency,sell_price,buy_price])




    markdown_table =f"Currency Exchange Rates in: {time_extracted.strftime('%Y-%m-%d %H:%M:%S')}"+"\n\n"+str(test_table)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    params = {
        "chat_id": chat_id,
        "text": markdown_table,
        "parse_mode": "markdown"
    }

    response = requests.post(url, params=params)
    print("sleeping")
    time.sleep(10)