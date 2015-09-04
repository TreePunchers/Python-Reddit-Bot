import praw
from bot_data import people
'''
people should be a dictionary with type
string: namedtuple('PersonData', ['skype_account', 'bot_account', 'bot_password'])
'''

r = praw.Reddit(user_agent='Test Script by /u/TreePunchers')
r.login('David_Ree_AI', 'dank_pass_123')
