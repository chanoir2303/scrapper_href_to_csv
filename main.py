import requests
from bs4 import BeautifulSoup
import pandas

url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser').find_all('a')
url_list = []

for i in soup:
    if str(i).startswith('http'):
        url_list.append(i.get('href'))
    else:
        url_list.append(url + str(i.get('href')))

x = pandas.DataFrame(url_list)
x.to_csv('output.csv')
print(len(url_list), 'links outputted')
