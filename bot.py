import praw
import random
from helper import generate_comment
from bot_data import people

'''
people should be a dictionary with type
string: namedtuple('PersonData', ['skype_account', 'bot_account', 'bot_password'])
'''


def post_comment(name, subreddit_name, min_words=20, words_per=50):
    r = praw.Reddit(user_agent='Reddit Markov Skype by /u/TreePunchers')
    r.login(people[name].bot_account, people[name].bot_password, disable_warning=True)
    subreddit = r.get_subreddit(subreddit_name)
    comment = generate_comment(name, min_words, words_per)
    if random.randint(0, 1) == 0:
        # Comment on recent comment
        post_on = list(subreddit.get_comments(limit=10))
        random.choice(post_on).reply(comment)
    else:
        # Comment on recent post
        post_on = list(subreddit.get_new(limit=10))
        random.choice(post_on).add_comment(comment)
    r.clear_authentication()


def post_with_random_user(subreddit_name, min_words=20, words_per=50):
    name = random.choice(list(people.keys()))
    post_comment(name, subreddit_name, min_words, words_per)

# Bot running protocol goes here:
# Example, posts 3 random comments.

for x in range(3):
    print(x)
    post_with_random_user('skypechatbottest')  # You will need to change this to a subreddit you have access to.