import requests
from bs4 import BeautifulSoup
url = "https://www.bonbast.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    currency_table = soup.find_all('table', class_='table-condensed')

    for table in currency_table:
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
        mine= columns[2]
        print(mine)
            # if columns:
            #     code = columns[0].text.strip()
            #     currency = columns[1].text.strip()
            #     sell_price = columns[2].text.strip()
            #     buy_price = columns[3].text.strip()
            #     print(f"Code: {code}, Currency: {currency}, Sell: {sell_price}, Buy: {buy_price}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")