import requests
from bs4 import BeautifulSoup
from datetime import date
from common_functions import *

def getNationalInterest(keywords, max_articles):
    count = 0

    home_page = "https://nationalinterest.org"

    out = open("links"+str(date.today())+".txt", "a")
    out.write("The National Interest\n\n")

    page = requests.get("https://nationalinterest.org/tag/military")
    soup = BeautifulSoup(page.content, "html.parser")

    main_article = soup.find("a", class_="article__link")
    stories = soup.find_all("a", class_="featured__link")
    articles = soup.find_all("div", class_="article__content")
    main_title = main_article.find("h2", class_="article__title").text
    if check_keywords(main_title, keywords):
        out.write(main_title + "\n")
        out.write("\t" + home_page + main_article["href"] + "\n")

    for story in stories:
        if count == max_articles:
            return
        story_title = story.find("h3", class_="featured__title").text
        if check_keywords(story_title, keywords):
            out.write(story_title + "\n")
            out.write("\t" + home_page + story["href"] + "\n")
            count += 1

    for article in articles:
        if count == max_articles:
            return
        article_title = article.find("a", class_=None).text
        article_link = article.find("a", class_=None)["href"]
        #article_date = article.find("span", class_="meta__date").text.split()
        if check_keywords(article_title, keywords):
            out.write(article_title + "\n")
            out.write("\t" + home_page + article_link + "\n")
            count += 1

    out.write("\n\n")

    out.close()