from bs4 import BeautifulSoup
import requests
import pprint
import csv
pp = pprint.PrettyPrinter()

URL = 'https://www.kivano.kg/noutbuki-i-kompyutery'
# ?page=2

def get_html(url):
    response = requests.get(url)
    return response.text

def get_all_pages(html):
    pages = []
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find('div', class_='pager-wrap').ul
    for li in ul:
        if li !='\n' and li.find('a') is not None:
            pages.append(li.find('a')['href'][12:])
    pages.pop(-1)
    pages.pop(-1)
    pages.pop(0)
    links = [URL +page for page in pages]
    links.insert(0, URL + '?page=1')
    return links

# print(get_all_pages(get_html(URL)))

def get_page_data(html):
    data = []
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_='list-view')
    print(divs)
    for div in divs:
        image = 'https://www.kivano.kg/' + div.find('img')['src']
        name = div.find('body', class_='listbox_title oh')
        price = div.find('w0', class_='listbox_price text-center')

        pc_data = [image, name, price]
        print(image)
        print(price)
        print(price)
        print(pc_data)

        data.append(pc_data)


    return data


def get_all_data():
    all_data = []
    all_pages = get_all_pages(get_html(URL))
    for page in all_pages:
        r = requests.get(page).text
        data = get_page_data(r)
        all_data.append(data)
    return all_data

# print(get_all_data())
(get_page_data(get_html(URL)))

