from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup as B
try:
    html = urlopen('https://coreyms.com/')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server is not found!')

bsobj = B(html.read(), 'lxml')
for article in bsobj.find_all('article'):
    title = article.h2.a.text
    content = article.div.p.text
    link = article.find('iframe', class_='youtube-player')
    print(title)
    print(content)
    print(link)
    print()
# print(get_into.h2.a.text)
# for i in bsobj.
# print(len(img))
# print(img[0].get_text())

# print(list(bsobj.body))
