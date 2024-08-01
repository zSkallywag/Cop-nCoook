import requests
from bs4 import BeautifulSoup



url_up= "https://www.nike.com/w/new-upcoming-drops-k0gk"


# Send an HTTP GET request to the website
response = requests.get(url_up)


soup = BeautifulSoup(response.content, 'html.parser')

div = soup.find('div', {'class': 'product-grid__items css-hvew4t'})

links = []
if div:
    a_tags = div.find_all('a')
    for a in a_tags:
        href = a.get('href')
        if href:
            links.append(href)

# Print the extracted links
t = 0
for link in links:
    t = t + 1
    print(t)
    print(link)
