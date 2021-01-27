import ars_technica
import national_interest
import popular_mechanics

from ars_technica import *
from national_interest import *
from popular_mechanics import *

keywords_file = open("topics.txt", "r")
keywords = list()

for word in keywords_file.readlines():
    keywords.append(word.rstrip())

max_articles = 5

getArsTechnica(keywords, max_articles)
getNationalInterest(keywords, max_articles)
getPopularMechanics(keywords, max_articles)