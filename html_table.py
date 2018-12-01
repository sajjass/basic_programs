import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
from csv import DictWriter

url = "http://www.espn.com/college-football/bcs?year=2013"
r=requests.get(url)
data=r.text

soup=BeautifulSoup(data,'html.parser')
tables=soup.findAll('table')

for table in tables:
    # The first tr contains the field names.
    headings = [th.get_text().strip() for th in table.find("tr").find_all("th")]
    print headings

    datasets = []
    for row in table.find_all("tr")[1:]:
        dataset = dict(zip(headings, (td.get_text().encode('utf-8') for td in row.find_all("td"))))
        datasets.append(dataset)

    keys = datasets[0].keys()

    with open('people.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(datasets)

    with open('spreadsheet.csv', 'w') as outfile:
        writer = DictWriter(outfile, keys)
        writer.writeheader()
        writer.writerows(datasets)