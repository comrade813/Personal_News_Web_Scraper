import requests
from bs4 import BeautifulSoup
from datetime import date
from common_functions import *

def parsePopularMechanics(url, out, keywords, count, max):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    stories = soup.find_all("div", {"class":["simple-item list-header-item", "simple-item grid-simple-item"]})
    for story in stories:
        if count == max:
            return count

        link = story.find("a")["href"]
        desc = story.find("div", class_="simple-item-title item-title").text

        if check_keywords(desc, keywords):
            out.write(desc+"\n")
            out.write("\t"+str(link)+"\n")
            count += 1

    return count

def getPopularMechanics(keywords, max_articles):
    count = 0
    out_file = open("links"+str(date.today())+".txt", "a")
    out_file.write("Popular Mechanics\n\n")
    count = parsePopularMechanics("https://popularmechanics.com/science", out_file, keywords, count, max_articles)
    parsePopularMechanics("https://popularmechanics.com/technology", out_file, keywords, count, max_articles)
    out_file.write("\n")
    out_file.close()