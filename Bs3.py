import requests
from bs4 import BeautifulSoup
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print(page.content)


soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('p')
soup.find_all('p')[0].get_text()
soup.find('p')