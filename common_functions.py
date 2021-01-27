from datetime import datetime

def check_date(date):
    today = datetime.now()
    month = str(today.strftime("%b"))
    day = str(today.strftime("%-d"))
    year = str(today.strftime("%Y"))
    return date[0] == month and date[1][:-1] == day and date[2] == year

def check_keywords(text, keywords):
    for s in keywords:
        if text.find(s) != -1 or text.find(s.lower()) != -1:
            return True
    return False