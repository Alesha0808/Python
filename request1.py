import requests
import time
from bs4 import BeautifulSoup

page = requests.get('https://ngs.ru')
soup = BeautifulSoup(page.text, 'html.parser')

links = soup.select('article[data-vr-contentbox]>h3>a')

news = []
for link in links:
    news.append({'title':link['title'], 'url':'https://ngs.ru'+link['href']})
time.sleep(1)

i = 0
notes = {}
notes['site'] = 'ngs.ru'
notes['news'] = []
for n in news:
    notes['news'].append({'id':i, 'title':n['title'],'nrl':n['url']})
    if i > 2: break
    i += 1
print(notes)