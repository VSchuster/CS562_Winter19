import nltk, string, sys
import math
import operator
import matplotlib

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

from collections import defaultdict


def remove_newlines(sentence):
    return sentence.rstrip("\r\n") + " "

def tokenize_sentences(sentences):
    tokenized = nltk.sent_tokenize(sentences)
    return tokenized

def remove_punctuation(tokens):
    punctuation_set = set(string.punctuation)
    no_punct_tokens = [t for t in tokens if t not in punctuation_set]
    return no_punct_tokens

def capitalize(tokens):
    tokens  = [token.upper() for token in tokens]
    return tokens

def tokenized_corpus(corpus):
    corpus = remove_newlines(corpus)
    corpus = tokenize_sentences(corpus)
    tokenized_corpus = [nltk.word_tokenize(sentence) for sentence in corpus]
    tokenized_corpus = [remove_punctuation(tokens) for tokens in tokenized_corpus]
    tokenized_corpus = [capitalize(tokens) for tokens in tokenized_corpus]
    return tokenized_corpus

processed = ''
with open(sys.argv[1], encoding='utf-16') as f:
    tokenized_corpus = tokenized_corpus(f.read())

print("Number of sentences: ", len(tokenized_corpus))

#########################################################
# Count and Comparing
#########################################################
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
    types = defaultdict(lambda: defaultdict(lambda: 0))
    for sentence in corpus:
        for i in range(len(sentence) - 1):
            prefix = tuple(sentence[i:i + 1])
            postfix = sentence[i + 1]
            types[prefix][postfix] += 1
    return types
        

def get_top_20_words(word_dict):
    top_twenty = sorted(word_dict, key=word_dict.get, reverse=True)[:20]
    return top_twenty

def remove_stop_words(word_dict):
    stop_words = set(stopwords.words('english')) 
    stop_words = [word.upper() for word in stop_words]
    for word in stop_words:
        if word in word_dict:
            del word_dict[word]
    return word_dict

unigram_tokens = get_unigram_tokens(tokenized_corpus)
num_unigram_types = len(unigram_tokens)
num_unigram_tokens = sum(unigram_tokens.values())
top_twenty = get_top_20_words(unigram_tokens)
no_stop_words = remove_stop_words(unigram_tokens)
top_twenty_no_stop_words = get_top_20_words(no_stop_words)
no_stop_types = len(no_stop_words)
no_stop_tokens = sum(no_stop_words.values())

bigram_dict = get_bigram_types(tokenized_corpus)

bigrams = nltk.bigrams(tokenized_corpus)
freq_dist = nltk.FreqDist(bigrams)
freq_dist.plot(30,cumulative=False)



print("Number of tokens: ", num_unigram_tokens)
print("Number of types: ", num_unigram_types)
print("Top Twenty: ", *top_twenty)
print("Top Twenty No Stop: ", *top_twenty_no_stop_words)
print("No Stop types: ", no_stop_types)
print("no stop tokens: ", no_stop_tokens)


############################
# Metrics
############################

def calculat_pmi(unigram_dict, bigram_dict):
    pass


