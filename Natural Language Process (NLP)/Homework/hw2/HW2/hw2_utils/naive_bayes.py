from hw2_utils.constants import OFFSET
from hw2_utils import clf_base, evaluation

import numpy as np
from collections import defaultdict, Counter
from itertools import chain
import math

# deliverable 3.1
def get_corpus_counts(x,y,label):
    """
    Compute corpus counts of words for all documents with a given label.

    :param x: list of counts, one per instance
    :param y: list of labels, one per instance
    :param label: desired label for corpus counts
    :returns: defaultdict of corpus counts
    :rtype: defaultdict

    """
    corpus_counts = defaultdict(lambda: 0)
    
    for index, value in enumerate(y):
        if value == label:
            for key in x[index]:
                corpus_counts[key] += x[index][key]
    
    return corpus_counts


# deliverable 3.2
def estimate_pxy(x,y,label,smoothing,vocab):
    """
    Compute smoothed log-probability P(word | label) for a given label. (eq. 2.30 in Eisenstein, 4.14 in J&M)

    :param x: list of counts, one per instance
    :param y: list of labels, one per instance
    :param label: desired label
    :param smoothing: additive smoothing amount
    :param vocab: list of words in vocabulary
    :returns: defaultdict of log probabilities per word
    :rtype: defaultdict of log probabilities per word

    """
    total_words = 0
    estimate = defaultdict(float)
    corpus_counts = get_corpus_counts(x,y,label)
    for key in corpus_counts:
        total_words += corpus_counts[key]
    
    bottom = total_words + len(vocab)
    
    for word in vocab:
        if word in corpus_counts:
            estimate[word] = np.log((corpus_counts[word] + smoothing) / bottom)
        else:
            estimate[word] = np.log(smoothing / bottom)
    
    return estimate
        
    
    

# deliverable 3.3
def estimate_nb(x,y,smoothing):
    """
    Estimate a naive bayes model

    :param x: list of dictionaries of base feature counts
    :param y: list of labels
    :param smoothing: smoothing constant
    :returns: weights, as a default dict where the keys are (label, word) tuples and values are smoothed log-probs of P(word|label)
    :rtype: defaultdict 

    """
    
    labels = set(y)
    #counts = defaultdict(float)
    #doc_counts = defaultdict(float)
    weights = defaultdict(float)
    
    vocab = set()
    for counter in x:
        vocab = set(counter) | vocab
    
    for label in labels:
        current_estimates = estimate_pxy(x,y,label,smoothing,vocab)
        for key in current_estimates:
            weights[(label, key)] = current_estimates[key]
    
    return weights
            
        
    
    
    

# deliverable 3.4
def find_best_smoother(x_tr,y_tr,x_dv,y_dv,smoothers):
    """
    Find the smoothing value that gives the best accuracy on the dev data

    :param x_tr: training instances
    :param y_tr: training labels
    :param x_dv: dev instances
    :param y_dv: dev labels
    :param smoothers: list of smoothing values
    :returns: best smoothing value, scores
    :rtype: float, dict mapping smoothing value to score
    """

    raise NotImplementedError
    