#!/usr/bin/env python
"""
#####################################################################
convert.py

Convert Google's pretrained word2vec model into a pickled dataframe.
See below for specific filter information

written by Lutz Hamel, (c) 2018 - University of Rhode Island
#####################################################################
"""

import pandas as pd
import gensim

#####################################################################
GOOGLE_MODEL = 'GoogleNews-vectors-negative300.bin'
NEW_MODEL = 'word2vec.pkl' # NOTE: has to be a pickle file name

#####################################################################
def load_gmodel(model_file):

    print("Loading Google's word2vec model...")
             
    return gensim.models.KeyedVectors.load_word2vec_format(
        model_file,
        binary=True)

#####################################################################
def convert(gmodel):
    '''
    convert googles model
    '''
    vec_list = []
    word_list = []

    model_vocab = list(gmodel.vocab.keys())

    print("converting model...")
    # iterate over Google's model and pull out the things
    # we are interested in.
    # NOTE: we only allow lower case words in the new model
    #       no numbers, punctuation etc.
    for word in model_vocab:
        if word.islower() and word.isalpha():
            vec_list.append(gmodel[word])
            word_list.append(word)

    # create our model from the vectors and index with the words
    model_df = pd.DataFrame(vec_list, index=word_list)

    # return our model
    return model_df

#####################################################################
# execute only if run as a script
if __name__ == "__main__":

    gmodel = load_gmodel(GOOGLE_MODEL)
    model_df = convert(gmodel)

    r,c = model_df.shape
    print("saving new model with {} words and {} dimensions...".format(r,c))
    model_df.to_pickle(NEW_MODEL)
    
            
