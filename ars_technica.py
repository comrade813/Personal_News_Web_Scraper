import requests
from bs4 import BeautifulSoup
from datetime import date
from common_functions import *

def parseArsTechnica(url, out, keywords, count, max):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    stories = soup.find_all("li", class_="tease article")

    for story in stories:
        if count == max:
            return count
        link = story.find("a", class_="overlay")["href"]
        desc = story.find("p", class_="excerpt").text
        #date  = story.find("time", class_="date").text.split()
        if check_keywords(desc, keywords):
            out.write(desc+"\n")
            out.write("\t"+str(link)+"\n")
            count += 1
    return count

def getArsTechnica(keywords, max_articles):
    count = 0
    out_file = open("links"+str(date.today())+".txt", "w+")
    out_file.write("Ars Technica\n\n")
    count = parseArsTechnica("https://arstechnica.com/gadgets", out_file, keywords, count, max_articles)
    parseArsTechnica("https://arstechnica.com/science", out_file, keywords, count, max_articles)
    out_file.write("\n")
    out_file.close()