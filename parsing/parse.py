from bs4 import BeautifulSoup
import requests
import pprint
import csv
pp = pprint.PrettyPrinter()

URL = 'https://ostore.kg/phones/'

csv_file = open('ostore.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['image', 'name', 'price'])

def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_pages(html):
    pages = []
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find('div', class_='bx-pagination-container').ul
    for li in ul:
        if li != '\n' and li.find('a') is not None:
            pages.append(li.find('a')['href'][8:])

    pages.pop(-1)
    links = [URL + page for page in pages]
    links.insert(0, URL + '?PAGEN_4=1')
    pp.pprint(links)
    return links


def get_page_data(html):
    data = []
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_ = 'item product sku')
    for div in divs:
        image = 'https://ostore.kg/' + (div.find('img')['src'])
        name = div.find('span', class_ = 'middle').text
        price = div.find('a', class_ = 'price').text
        phone_data = [image, name, price]
        data.append(phone_data)

    return data

def get_all_data():
    all_data = []
    all_pages = get_all_pages(get_html(URL))

    for page in all_pages:
        r = requests.get(page).text
        data = get_page_data(r)
        all_data.append(data)
        # pp.pprint(data)

    return all_data


# get_all_data(get_html(URL))
# get_page_data(get_html(URL))
def save_data(data):
    # d = [i for l in data for i in l]
    phone_data = [phone for page in data for phone in page]
    for phone in phone_data:
        csv_writer.writerow(phone)

save_data(get_all_data())