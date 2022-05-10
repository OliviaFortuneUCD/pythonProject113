# importing the libraries
from bs4 import BeautifulSoup
import requests


page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)")


soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.find_all("a"):
    print("Inner Text: {}".format(link.text))
    print("Title: {}".format(link.get("title")))
    print("href: {}".format(link.get("href")))