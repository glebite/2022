"""
"""
import requests
from bs4 import BeautifulSoup
import re
import json

MAIN_URL = "https://www.einpresswire.com/world-media-directory/3/canada"
BASE_URL = "https://www.einpresswire.com"

def get_id(link):
    matches = re.search(r"([a-z\-\/]*)([0-9]*)", link)
    return matches.group(2)

if __name__ == "__main__":
    scratch = requests.get(MAIN_URL).text
    soup = BeautifulSoup(scratch, features='lxml')
    columns = soup.findAll("div", {"class": "col-sm-6"})

    media_storage = {}
    
    for column in columns:
        media = column.findAll("div", {"class": "sl-heading"})
        for counter, item in enumerate(media):
            print(counter)
            anchor = item.find("a")
            link = anchor.get('href')
            id = get_id(link)
            media_storage[id] = {}
            individual = requests.get(BASE_URL + link)
            souper = BeautifulSoup(individual.text, features='lxml')
            table = souper.find("table", {"class": "simple full"})
            rows = table.findAll("tr")
            c = 0
            for row in rows:
                th = row.find("th")
                td = row.find("td")
                if not th:
                    continue
                if td:
                    key = th.text.strip()
                    if key in media_storage[id]:
                        key = key + str(c)
                        print(f'\t\t\t\{key}')                        
                        c += 1
                    media_storage[id][key] = td.text.strip()
    with open('media_data.json', 'w') as fp:
        json.dump(media_storage, fp, indent=4)

        
