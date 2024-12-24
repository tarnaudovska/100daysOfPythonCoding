from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a", class_="storylink")
article_text = article_tag.getText()
article_link = article_tag.get('href')
print(article_link)


# import lxml

# with open("./day_45/bs4-start/website.html") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")

# heading = soup.find(name="h1", id = "name")
# print(heading)