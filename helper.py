import pickle
from markovgen import Markov
from bot_data import people
'''
People should be a dictionary with type
string: namedtuple('PersonData', ['skype_account', 'bot_account', 'bot_password'])
'''


def generate_comment(author, min_words=20, words_per=50):
    def generate_comment_part(markov):
        part = markov.generate_markov_text(words_per)
        return part.capitalize()

    messages = load_obj('skype_messages')
    author_markov = Markov(messages[people[author].skype_account])
    result = ''
    while len(result.split(' ')) < min_words:
        result += generate_comment_part(author_markov).replace('\n', '').replace('\r', '') + '. '
    return result


def save_obj(obj, name):
    with open('obj/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
