"""
"""
import requests
from bs4 import BeautifulSoup
import re

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }


def google(q):
    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    r = s.get(url, headers=headers_Get)

    soup = BeautifulSoup(r.text, "html.parser")
    output = []
    print(soup.body.h3)

    
    # for searchWrapper in soup.find_all('h3'): #this line may change in future based on google's web page structure
    #     url = searchWrapper.find('a')["href"] 
    #     text = searchWrapper.find('a').text.strip()
    #     result = {'text': text, 'url': url}
    #     output.append(result)

    return output



if __name__ == "__main__":
    scratch = requests.get('https://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government').text
    soup = BeautifulSoup(scratch, features='lxml')
    table = soup.find("table", {"class": "wikitable plainrowheaders"})

    rows = table.findAll(lambda tag: tag.name=='tr')
    for row in rows:
        th = row.find("th", {"scope": "row"})
        if th:
            anchor = th.find("a")
            country = anchor.text
        td = row.find("td", {"style": re.compile(r".*")})
        if td:
            anchors = td.findAll("a")
            if len(anchors) >= 2:
                print(f'official {anchors[0].text} website {country}')
                print(f'official {anchors[1].text} website {country}')
            else:
                print("\tInteresting...")
