import requests
from bs4 import BeautifulSoup

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD : ")
URL = "https://www.billboard.com/charts/hot-100/2020-10-20/"
response = requests.get(url= URL)

ALL_TITLES = []

soup = BeautifulSoup(response.text, 'html.parser')
all_blocks = soup.find_all(name = "div", class_ = "o-chart-results-list-row-container")
for block in all_blocks:
    title = block.find('h3', id = "title-of-a-story").getText().strip()
    ALL_TITLES.append(title)

print(ALL_TITLES)