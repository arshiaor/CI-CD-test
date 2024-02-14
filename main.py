import requests,os,tokens
from selenium import webdriver
import time,datetime,pytz
from prettytable import PrettyTable
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

bot_token= tokens.bot_token
chat_id= tokens.chat_id
api_id= tokens.api_id
api_hash= tokens.api_hash

while True:
    result_table=PrettyTable(["Currency","Sell","Buy"])
    gold_table=PrettyTable(["Gold Coin", "Sell", "Buy"])
    start_time = time.time()
    url = 'https://www.bonbast.com/'
    # options = webdriver.ChromeOptions()
    options = webdriver.chrome.options.Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    # driver = webdriver.Chrome(service=ChromeService(), options=options)
    chrome_driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(options=options)

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
    # time.sleep(600)
    time.sleep(120)