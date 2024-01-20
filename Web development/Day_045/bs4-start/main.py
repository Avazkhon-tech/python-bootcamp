import soupsieve
from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
spans = soup.find_all(name="span", class_="titleline")
articles = []
for span in spans:
    articles.append(span.find("a"))

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    # print(text)
    link = article_tag.get("href")
    # print(link)
    article_texts.append(text)
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

for i in range(len(article_texts)-1):
    print(article_texts[i])
    print(article_links[i])
    print(article_upvotes[i])
# print(len(article_texts))
# print(len(article_links))
# print(len(article_upvotes))

max_num = 0
index = 0
max_num_index = 0
for vote in article_upvotes:
    if max_num < vote:
        max_num = vote
        max_num_index = index
    index += 1
print(max_num_index)
print(article_upvotes[max_num_index])
print(article_links[max_num_index])
print(article_texts[max_num_index])





# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
#
# all_anchor_tags = (soup.find_all(name="a"))
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)

