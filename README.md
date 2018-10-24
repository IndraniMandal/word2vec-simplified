# Word2Vec Simplified

Google's original pretrained word2vec model consists of 3mil entries and its 
binary representation as a file is 3.5GB.  Both the size and the fact
that it is in a non-standard binary representation makes this model difficult
to work with - you basically have to take the plunge and learn 'gensim'.

The goal of this project is to provide a smaller, easier to work with model
for the use in Python.  The model consists of a pickled Pandas DataFrame where 
each row represents the embedding of a particular word and each column is 
one of the dimensions of the embedding space.  The row index is comprised of 
the words in this model. This model only contains single, lower case words with no punctuation etc.

This github repository provides the code for the conversion from the Google 
model to our DataFrame based model.

* **convert.py** - Python program to convert the Google model
* **word2vec.py** - Example program that uses our DataFrame based model

## Prerequisites

1. The model and the code assumes that you have Python 3.x installed.
2. The conversion code assumes that you have downloaded and unzipped Googles 
original model GoogleNews-vectors-negative300.bin from [here](https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz).
