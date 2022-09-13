from wsgiref import headers
import html5lib
import requests
from bs4 import BeautifulSoup

url = r"https://www.airdna.co/vacation-rental-data/app/us/california/santa-monica/overview"
data = requests.get(url)
#print(data.content)

soup = BeautifulSoup(data.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())
