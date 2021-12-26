# https://github.com/jorgegonzalez/beginner-projects#random-wikipedia-article

import requests, webbrowser


def get_articles():
    r = requests.get('https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json')
    articles = r.json()['query']['random']
    return articles


# Main event
print("|---------[Random Wikipedia Article]---------|")
running = True
while running:
    new_articles = get_articles()
    for article in new_articles:
        response = ""
        while response not in ('y','n','QUIT'):
            response = input(f"Do you want to read {article['title']}? [y/n/QUIT]\n>>> ")
        if response == 'y':
            webbrowser.open(f'https://en.wikipedia.org/wiki?curid={article["id"]}', new=2)
            input("Press ENTER when you're done reading.\n")
        elif response == 'QUIT':
            print("Thanks for using!!\nHave a nice day \(^o^)/")
            running = False
            break