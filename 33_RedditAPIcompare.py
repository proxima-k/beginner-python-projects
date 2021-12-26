# https://github.com/jorgegonzalez/beginner-projects#compare-recent-reddit-karma
# Finished at 26 Apr 2020
import praw, prawcore, time

reddit = praw.Reddit(client_id = 'xxx',
                     client_secret = 'xxx',
                     user_agent = 'xxx',
                     username='xxx',
                     password= 'xxx')

class Program():
    def __init__(self):
        self.redditor_list = []
        self.running = True
        while self.running:
            self.main()
            self.repeat()

    def user_exists(self, name):
        try:
            reddit.redditor(name).id
        except prawcore.NotFound:
            print("This user does not exist. You sure you typed the correct username??")
            return None
        except RecursionError:
            print("You didn't type anything.")
            return None
        else:
            print("User found.\n")
            return reddit.redditor(name)

    def get_user(self):
        name_1 = input("Insert the first user's name here\n>>> ")
        redditor_1 = self.user_exists(name_1)

        name_2 = input("Insert the second user's name here\n>>> ")
        redditor_2 = self.user_exists(name_2)

        self.redditor_list.append(redditor_1)
        self.redditor_list.append(redditor_2)

    def compare_score(self):
        for submission in self.redditor_list[0].submissions.new(limit=1):
            self.display_post_details(submission)
            score_1 = submission.score
        for submission in self.redditor_list[1].submissions.new(limit=1):
            self.display_post_details(submission)
            score_2 = submission.score

        print('Analysing...')
        time.sleep(2)
        if score_1 > score_2:
            print(f'<{self.redditor_list[0].name}> has a higher score than <{self.redditor_list[1].name}>')
        else:
            print(f'<{self.redditor_list[1].name}> has a higher score than <{self.redditor_list[0].name}>')
        diff_ = abs(score_1 - score_2)
        print(f'with a difference of {diff_}.\n')

    def display_post_details(self, submission):
        print('|-----------------------|')
        print(f'User: {submission.author}')
        print(f'Post Title: {submission.title}')
        print(f'Upvotes: {submission.ups}')
        print(f'Downvotes: {submission.downs}')
        print('|-----------------------|')
        print()

    def main(self):
        self.get_user()
        for redditor in self.redditor_list:
            if redditor == None:
                print("Looks like there's nothing to compare :)\nPlease try again.")
                return
            if len(list(redditor.submissions.new(limit=1))) == 0:
                print(f'User with the name {redditor.name} hasn\'t post anything.')
                return
        self.compare_score()

    def repeat(self):
        ask = ''
        while ask.lower() not in ('y', 'n'):
            ask = input("Do you still want to compare scores? [y/n]\n>>> ")
        if ask.lower() == 'n':
            self.running = False
        elif ask.lower() == 'y':
            pass

program = Program()
print("Ok. Thanks for using.\nHave a nice day! \\(^o^)/")