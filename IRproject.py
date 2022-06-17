import requests
from bs4 import BeautifulSoup
from newspaper import Article
from tqdm import tqdm
import pandas as pd
import requests

def sctrap_page(page) :
    print(page)
    urls = []
    page_url = f"https://alefbyte.ir/category/%d9%86%d9%82%d8%af-%d9%88-%d8%a8%d8%b1%d8%b1%d8%b3%db%8c/page/{page}/"
    html = requests.get(page_url).text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('h3')
    # print(links)
    for x in links:
        try:
            page_url = x.a['href']
            urls.extend(page_url)
            # print(page_url)
            # print(x.a['href'])
        except:
            print('')
    print(urls)

    # print(links)
sctrap_page(2)