from cgitb import html
from bs4 import BeautifulSoup
import requests

# url = "https://transparentcalifornia.com/salaries/search/?q=superintendent&y=2020&page=1"
# r = requests.get(url)
# html_doc = r.text

# soup = BeautifulSoup(html_doc)

# #pretty_soup = soup.prettify()

# names = soup.find_all('a')

# for name in names:
#     print(name.string)

# url = 'https://www.california-demographics.com/cities_by_population'
# r = requests.get(url)
# html_doc = r.text
# soup = BeautifulSoup(html_doc, "lxml")

# # Find the table body
# tbody = soup.tbody

# # Finds all the table rows
# trs = tbody.contents

# print(trs)

##### Coinbase test web scraper 

url = 'https://coinmarketcap.com/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)

tbody = soup.tbody

print(tbody)