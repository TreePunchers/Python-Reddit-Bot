import random


class Markov(object):
    def __init__(self, user_messages):
        self.cache = {}
        self.user_messages = user_messages
        self.database()

    def triples(self):
        for message_chain in self.user_messages:
            split_chain = message_chain.split(' ')
            if len(split_chain) < 3:
                continue
            else:
                for i, _ in enumerate(split_chain[:-2]):
                    yield (split_chain[i], split_chain[i + 1], split_chain[i + 2])

    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_markov_text(self, size=25):
        seed = random.choice(list(self.cache.keys()))
        seed_word, next_word = seed[0], seed[1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)
            try:
                w1, w2 = w2, random.choice(self.cache[(w1, w2)])
            except KeyError:
                break
        gen_words.append(w2)
        return ' '.join(gen_words)
