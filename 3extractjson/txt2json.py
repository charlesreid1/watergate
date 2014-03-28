from numpy import *
#import nltk
from nltk.tokenize import *
import re
import sys
import os
from os.path import splitext
from os.path import basename


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

    # 118 text files.
    # Text cleanup that needs to happen:
    # - header and only header on first line and only first line
    # - line of dialogue on each one
    # - names split up and corrected
    # - typos/unsplit words fixed

    # re for all-caps words (i.e., the names)
    # - RegexpTokenizer: https://nltk.googlecode.com/svn/trunk/doc/howto/tokenize.html
    # - the regex: http://stackoverflow.com/questions/4598315/regex-to-match-only-uppercase-words-with-some-exceptions
    allnames = RegexpTokenizer('[A-Z]{3,}\w').tokenize(data)
    names = unique(allnames)

    for name in names:
        occur = data.count(name)
        if occur < 3:
            del allnames[ allnames.index(name) ]
            names = unique(allnames)# update names

    d_indx = {}

    # pad names with whitespace to make parsing easier
    for name in names:
        data = data.replace(name,' '+name+'\n')

    # obtain index of each occurrence of each name
    for name in names:
        d_indx[name] = [m.start() for m in re.finditer(name,data)]
        print "Name",name,"occurs at indices:"
        print d_indx[name]

    all_indx = []
    for k in d_indx.keys():
        all_indx += d_indx[k]
    all_indx.sort()



    # now we can chop the data up into 
    # - header
    # - dialogue
    # - footer

    # then further process each piece.
    # further processing means extracting
    # and parsing relevant details, and
    # putting that all into JSON structure.



    # header:
    # everything up until the occurrence of the first name
    header = data[0:all_indx[0]]

    # body:
    # everything else
    body = data[all_indx[0]:]

    # footer:
    # there is no footer



    # Now turn this into JSON


    # Consideration: there are probably multiple formats.
    # Take a quick look to determine how they group up.
    # Divide them by directory.

