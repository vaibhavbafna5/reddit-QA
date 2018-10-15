import requests
import spacy
from bs4 import BeautifulSoup
import re
import praw
from praw.models import MoreComments

#client_id: jhAffV3EzTf80A
#secret: f38Y5S9QTzm6y0LyG5UiU47sMKk
#username: carameldeligh5
#password: @Collingsworth5

term = "best places to eat in seattle reddit"
substring = "comments/"

def scrape_google(term):
    page = requests.get("https://www.google.com/search?q=" + term)
    soup = BeautifulSoup(page.content, "lxml")
    links = soup.select(".r a")
    return ["https://www.google.com" + link.get('href') for link in links]

links = scrape_google(term)
links = links[1:]

submissions = []

for link in links: 
    print ("LINK: " + link)
    print ("\n")
    begIndex = link.index(substring) + 9
    endIndex = begIndex + 6
    submissions.append(link[begIndex : endIndex])
    print (link[begIndex:endIndex] + "\n")

client_id = "jhAffV3EzTf80A"
client_secret = ""
username = ""
password = ""

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='testscript by /u/carameldelight5',
                     username=username)
                     
count = 0 
for submissionID in submissions: 
    print (count)
    submission = reddit.submission(id = submissionID)

    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        print(top_level_comment.body)

    count += 1

# https://www.google.com/url?q=https://www.reddit.com/r/SeattleWA/comments/8l3nru/best_of_seattle_ethnic_cuisine/&sa=U&ved=0ahUKEwi_mJephrfcAhUbCDQIHW8lAPUQFghEMAU&usg=AOvVaw1wvmszgTSr5WHBFy0O9d_9

