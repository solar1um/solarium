from bs4 import BeautifulSoup
import requests
import pprint
import csv
pp = pprint.PrettyPrinter()

URL = 'https://www.kivano.kg/noutbuki-i-kompyutery'

def get_html(url):
    r = requests.get(url)
    return r.text

# def get_all_pages(html):
#     pages = []
#     soup = BeautifulSoup(html, 'html.parser')
#     ul = soup.find('div', class_='listbox_title oh').ul
    # for li in ul:
    #     if li != '\n' and li.find('a') is not None:
    #         pages.append(li.find('a')['href'][8:])

    # pages.pop(-1)
    # links = [URL + page for page in pages]
    # links.insert(0, URL + '?page=1')
    # pp.pprint(links)
    # return links


def get_page_data(html):
    data = []
    soup  = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_='item product_listbox oh')
    for div in divs:
        image = 'https://kivano.kg/' + (div.find('img')['src'])
        name = div.find('a', 'alt')
    return image



print(get_page_data(get_html(URL)))
# get_all_pages(get_html(URL))
# get_all_pages(get_html(URL))