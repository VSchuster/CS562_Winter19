from  hw2_utils import constants 
import numpy as np

# deliverable 4.1
def get_token_type_ratio(counts):
    """
    Compute the ratio of tokens to types
    
    :param counts: bag of words feature for a song
    :returns: ratio of tokens to types
    :rtype float
    """
    types = set()
    tokens = 0.0
    types = types | set(counts)
    for key in counts:
        tokens = counts[key] + tokens
            
    return tokens / len(types)
    
    

# deliverable 4.2
def concat_ttr_binned_features(data):
    """
    Add binned token-type ratio features to the observation represented by data
    
    :param data: Bag of words
    :returns: Bag of words, plus binned ttr features
    :rtype: dict
    """
    
    data[OFFSET] = 0
    data[TTR_ZERO] = 0
    data[TTR_ONE] = 0
    data[TTR_TWO] = 0
    data[TTR_THREE] = 0
    data[TTR_FOUR] = 0
    data[TTR_FIVE] = 1
    data[TTR_SIX] = 0
    
    return data
    

