import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "http://www.espn.com/college-football/bcs?year=2013"

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

res = requests.get(url, headers=header)
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))
print(tabulate(df[0], headers='keys', tablefmt='psql'))
