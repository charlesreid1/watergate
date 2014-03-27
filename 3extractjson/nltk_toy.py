from numpy import *
import nltk
import sys
import os
from os.path import splitext
from os.path import basename

from nltk.tokenize import *

"""
Loads a single text file in.
Tokenizes it with natural language toolkit NLTK.
This is to perfect the technique.
"""

datdir = '../1primarytexts/txt/'

# get list of txt files
filenames = []
for nf,f in enumerate( os.listdir(datdir) ):
    if f.endswith(".txt") and nf==0:
        filenames.append( basename( splitext(f)[0] ) )

for myfile in filenames:

    data = ""
    with open (datdir+myfile+'.txt', "r") as mydat:
        data += mydat.read().replace('\n', '').replace('.','. ')

    # Text cleanup that needs to happen:
    # - header and only header on first line and only first line
    # - line of dialogue on each one
    # - names split up and corrected
    # - typos/unsplit words fixed
    #
    # On 118 text files.

    # re for all-caps words (i.e., the names)
    # - RegexpTokenizer: https://nltk.googlecode.com/svn/trunk/doc/howto/tokenize.html
    # - the regex: http://stackoverflow.com/questions/4598315/regex-to-match-only-uppercase-words-with-some-exceptions
    tokens2 = RegexpTokenizer('[A-Z]{3,}').tokenize(data)
    print unique(tokens2)
    for name in tokens2:
        data = data.replace(name,' '+name+'\n')

    # Plain ol nltk word tokenizer
    # http://stackoverflow.com/questions/15057945/how-do-i-tokenize-a-string-sentence-in-nltk
    tokens1 = nltk.word_tokenize(data)
    print sort(tokens1)

    ### # Header is everything up until first occurrence
    ### # of a name.
    ### first_occurs = [tokens1.index(name) for name in tokens2]
    ### first_occur = min(first_occurrences)
    ### header = tokens1[:first_occur]

