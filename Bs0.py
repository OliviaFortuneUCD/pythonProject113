# importing the libraries
from bs4 import BeautifulSoup
import requests


page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)")


soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('p')
soup.find_all('p')[0].get_text()
soup.find('p')
print(soup.title)
print(soup.title.text)