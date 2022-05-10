# importing the libraries
from bs4 import BeautifulSoup
import requests


page = requests.get("https://www.corkairport.com/arrivals-departures")



soup = BeautifulSoup(page.content, 'html.parser')
#soup.find_all('p')
#soup.find_all('p')[0].get_text()
#soup.find('p')
#print(soup)

#non_nested_tables = [t for t in soup.find_all('table') if not t.find_all('table')]
#print(non_nested_tables)

 

