import requests
from bs4 import BeautifulSoup


def getGithub():
    headers = {
        'Host': 'github.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    proxies = {
        'http': '10.167.219.228:8118',
        'https': '10.167.219.228:8118'
    }
    res = requests.get(url='https://github.com/MarryYou?tab=repositories',
                       headers=headers)
    if res.status_code == 200:
        res.encoding = 'utf-8'
        html = BeautifulSoup(res.text, 'lxml').find(
            'div', attrs={'id': 'user-repositories-list'}).find('ul')
        openSources = []
        for child in html.contents:
            if child.name != None:
                url = child.find('a')['href']
                title = child.find('a').string
                desc = None if child.find(
                    'p') == None else child.find('p').string
                svg = child.find(
                    'svg', attrs={'class': 'd-inline-block tooltipped tooltipped-s'})
                lang = child.find('div', attrs={'class': 'f6 text-gray mt-2'})
                source = {
                    'url': 'https://github.com' + url,
                    'title': title,
                    'desc': desc,
                    'svg': svg,
                    'lang': lang
                }
                openSources.append(source)
        return openSources
