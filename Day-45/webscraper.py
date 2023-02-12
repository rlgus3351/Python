from bs4 import BeautifulSoup
import requests
import numpy as np


response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name= "a", class_ = "titlelink")
articles_texts = []
articles_links = []
articles_upvotes = []
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span" , class_ = "score")]
# print(articles_texts)
# print(articles_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(articles_texts[largest_index])
print(articles_links[largest_index])

