import Deserializer as d
import math
import operator

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

from collections import defaultdict


def get_unigram_tokens(corpus):
    types = dict()
    for sentence in corpus:
        for word in sentence:
            if word not in types:
                types[word] = 0
            else:
                types[word] = types[word] + 1
    return types

def get_bigram_types(corpus):
    pass

def get_top_20_words(word_dict):
    top_twenty = list()
    for i in range(20):
        top_key = max(word_dict.iteritems(), key=operator.itemgetter(1))[0]
        top_twenty.append(max)
        word_dict.pop(top_key, None)
    return top_twenty

def remove_stop_words(word_dict):
    stop_words = set(stopwords.words('english')) 
    for word in stop_words:
        if word in word_dict:
            del word_dict[word]
    return word_dict
        
            




corpus = ""
unigram_tokens = get_unigram_tokens(corpus)
unigram_types = len(unigram_tokens)


#bigram_types = get_types(corpus, 2)
#bigram_tokens = get_tokens(corpus, 2)
