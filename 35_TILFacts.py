# https://github.com/jorgegonzalez/beginner-projects#watch-for-new-til-facts
# Finished at 27 Apr 2020
import praw, re, time
from praw import exceptions

reddit = praw.Reddit(client_id = 'xxx',
                     client_secret = 'xxx',
                     user_agent = 'xxx',
                     username = 'xxx',
                     password = 'xxx')
subreddit = reddit.subreddit('todayilearned')


def structure_change(str):
    pattern_front = r'TIL[\s|\:]*(that\s|\-\s)*'
    pattern_end = r'(\."|\.)$'
    if re.match(pattern_front, str):
        new_str = re.sub(pattern_front, '', str, 1)
        new_str = new_str[0].upper() + new_str[1:]
        if re.search(pattern_end, new_str):
            pass
        elif new_str[-1] == ' ':
            new_str = new_str[:-1] + '.'
        else:
            new_str = new_str + '.'
        return new_str
    else:
        return str

old_fact = ''
new_fact = ''
new_fact_link = ''

while True:
    for submission in subreddit.new(limit=1):
        new_fact = submission.title
        new_fact = structure_change(new_fact)
        new_fact_link = submission.url
    if new_fact != old_fact:
        with open('til_facts.txt', 'a') as f:
            f.write('\n')
            f.write(new_fact + '\n')
            f.write(f'Link >>> {new_fact_link}\n')
        old_fact = new_fact
        print(new_fact)
        print(f'Link >>> {new_fact_link}')
        print()

    time.sleep(30)