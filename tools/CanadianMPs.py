"""
Ugly quickie hack to retrieve the names of MPs and their emails from
the government website.
"""
import requests
from bs4 import BeautifulSoup
import re

BASE_URL = "https://www.ourcommons.ca/"

if __name__ == "__main__":
    scratch = requests.get(BASE_URL + 'members/en/' + 'search?view=list').text
    soup = BeautifulSoup(scratch, features='lxml')
    table = soup.find("tbody")

    rows = table.findAll(lambda tag: tag.name=='tr')
    for row in rows:
        tds = row.findAll("td")
        for td in tds:
            print(f'{td.text.strip()}, ', end='')
            anchor = td.find("a")
            if anchor and "constituencies" not in anchor.get('href'):
                link =  anchor.get('href')[1:]
                full_link = BASE_URL + link + '#contact'
                detail_page = requests.get(BASE_URL + link + '#contact')
                souper = BeautifulSoup(detail_page.text, features='lxml')
                anchors = souper.findAll("a")
                for a in anchors:
                    if "mailto:" in str(a):
                        print(f'{a.text}, ' , end='')
        print()
