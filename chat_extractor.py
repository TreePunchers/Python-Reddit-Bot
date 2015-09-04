import sqlite3
import warnings
from html import unescape
from bs4 import BeautifulSoup
from collections import defaultdict
from helper import save_obj

warnings.filterwarnings('ignore', category=UserWarning)
main = sqlite3.connect('main.db')


# Functions
def xml_decoded(data_string):
    soup = BeautifulSoup(data_string)
    [x.extract() for x in soup.findAll('quote')]
    return unescape(soup.get_text())


results = defaultdict(list)
prev_author = ''
current_message_chain = ''

for data in main.execute(u"SELECT author, body_xml FROM Messages WHERE convo_id=1108 AND body_xml IS NOT NULL AND author IS NOT ''"):
    current_author = data[0]
    if current_author == prev_author:
        # Continue message chain
        current_message_chain += u' ' + xml_decoded(data[1])
    elif current_author != prev_author:
        # Deposit old message chain
        results[prev_author].append(current_message_chain)
        # Start a new one
        current_message_chain = xml_decoded(data[1])
    prev_author = current_author

save_obj(results, 'skype_messages')
print('Skype message file updated!')
