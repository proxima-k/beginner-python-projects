# https://github.com/jorgegonzalez/beginner-projects#website-scraper--analyzer
import requests, re, time
from bs4 import BeautifulSoup

url = input("Please insert the url here: ")
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
score = 0


# ____________________[HEAD SECTION]_______________________________
# TITLE
title = soup.find('title')
if title:
    print('- title tag found!')
    score += 1


# DESCRIPTION
description = soup.find_all('meta', attrs={'name' : 'description'})
if description:
    print('- description found!')
    score += 2


# MOBILE-FRIENDLY
m_width = soup.find('meta', attrs={'content': 'width=device-width, initial-scale=1'})
if m_width:
    print('- mobile-friendly tag found!')
    score += 2


# ROBOTS
robot = soup.find('meta', attrs={'name' : 'robots'})
if robot:
    score += 5
    print(f'- robot tag found!')

# TWITTER CARDS
twitter = soup.find_all('meta', attrs={'name' : re.compile(r'twitter')})
if twitter:
    score += len(twitter)
    print(f'- twitter card tag found! ({len(twitter)})')


# OPEN GRAPH
open_graph = soup.find_all('meta', attrs={'property' : re.compile(r'og')})
if open_graph:
    score += 2
    print(f'- open graph tag found! ({len(open_graph)})')


# CANONICAL
canonical = soup.find('link', attrs={'rel' : 'canonical'})
if canonical:
    score += 3
    print('- canonical tag found!')


# ____________________[BODY SECTION]_________________________
# HEADERS <h1> - <h6>
headers = soup.find_all(re.compile(r'h[1-6]'))
if headers:
    score += len(headers) // 2
    print(f'- header tags found! ({len(headers)})')


# NO FOLLOW LINKS
nofollow = soup.find_all('a', attrs={'rel' : 'nofollow'})
if nofollow:
    score += len(nofollow)
    print(f'- nofollow attribute value found! ({len(nofollow)})')


# IMAGE ALTERNATIVE
img_alt = soup.find_all('img', attrs={'alt' : True})
if img_alt:
    score += len(img_alt)
    print(f'- image alternative found! ({len(img_alt)})')



# Results
print('\nAnalyzing score', end='')
for x in range(3):
    time.sleep(1)
    if x != 2:
        print('.', end='')
    else:
        print('.')
        time.sleep(1)

print(f'Overall Score: {score}')
