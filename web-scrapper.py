from bs4 import BeautifulSoup
import requests

url = "https://transparentcalifornia.com/salaries/search/?q=superintendent&y=2020&page=1"
r = requests.get(url)
html_doc = r.text

soup = BeautifulSoup(html_doc)

#pretty_soup = soup.prettify()

names = soup.find_all('a')

for name in names:
    print(name.string)
