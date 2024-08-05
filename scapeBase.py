import requests
from bs4 import BeautifulSoup

def extractLinks(url, class_name, tag):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', {'class': class_name})
    links = []
    
    if div:
        aTags = div.find_all(tag)
        
        for a in a_tags:
            href = a.get('href')
            if href:
                links.append(href)
    
    return links