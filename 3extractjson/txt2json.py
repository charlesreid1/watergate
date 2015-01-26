from numpy import *
import simplejson as json
#import nltk
from nltk.tokenize import *
import re
import sys
import os
from os.path import splitext
from os.path import basename


"""
Loads and parses a single text file.

Turns it into JSON.

The strategy needs to apply to the 
(so far) 118 text files.

Text cleanup that needs to happen:
* Split text into header / body / footer
* Find names (identified by ALLCAPS)
* Parse text into names and text

so something like
HUNT:Well, uh, about as can be expected. How areyou?COLSON:Uh, just about the same Christ tryin' to holdthe pieces together.

becomes
["HUNT",
"Well, uh, about as can be expected. How areyou?",
"COLSON",
"Uh, just about the same Christ tryin' to holdthe pieces together."
]

This will eventually become:
{"tokens":["Well, uh, about as can be expected.","How are you?"], "speaker":"HUNT"}
{"tokens":["Uh, just about the same Christ tryin' to holdthe pieces together."], "speaker":"COLSON"}

Which is JSON that olipy can understand.
"""

datdir = '../1primarytexts/txt/'

# get list of txt files
filenames = []
for nf,f in enumerate( os.listdir(datdir) ):
    if f.endswith(".txt"):# and nf==0:
        filenames.append( basename( splitext(f)[0] ) )


for myfile in filenames:

    print "\n"
    print "-"*45
    print "Working on file "+myfile

    data = ""
    with open (datdir+myfile+'.txt', "r") as mydat:
        data += mydat.read().replace('\n', ' ').replace('.','. ').replace('?','? ')



    # regexp for all-caps words (i.e., the names)
    # - RegexpTokenizer: https://nltk.googlecode.com/svn/trunk/doc/howto/tokenize.html
    # - the regex: http://stackoverflow.com/questions/4598315/regex-to-match-only-uppercase-words-with-some-exceptions
    allnames = RegexpTokenizer('[A-Z]{3,}\w').tokenize(data)
    names = unique(allnames)

    for name in names:
        occur = data.count(name)
        if occur < 3:
            del allnames[ allnames.index(name) ]
            names = unique(allnames)# update names

    print "-"*45
    print "Found the following names in transcript:"
    print names
    print "-"*45

    d_indx = {}

    # pad names with whitespace to make parsing easier
    for name in names:
        data = data.replace(name+':',' '+name+' ')

    # Now we want to split the string 
    # at each occurrence of each name.
    # 
    # re.split('THIS|THAT|OTHER',mystring)
    #
    # First, assemble the re:
    names_regexp = "("
    for name in names:
        names_regexp += name
        names_regexp += "|"
    # Cut off the last |
    names_regexp = names_regexp[:-1]
    names_regexp += ")"

    try:
        data2 = re.split(names_regexp,data)
    except:
        pass

    # trim whitespace
    for j, token in enumerate(data2):
        data2[j] = token.strip()

    #print data2 

    master_list = []
    for itoken,token in enumerate(data2):

        if itoken==0:
            pass
        elif token in names:
            try:
                master_list.append(d)
            except:
                pass
            d = {}
            d['speaker'] = token
            d['tokens'] = []
        else:
            sentences = token.split('. ')
            for sentence in sentences:
                if sentence <> '':
                    d['tokens'].append(sentence+'.')

    import json
    final_file_text = ''
    for z in master_list:
        final_file_text += json.dumps(z)
        final_file_text += '\n'

    with open('watergate_2.json', 'a+') as outfile:
        outfile.write(final_file_text)


        


    ### # Okay, ALMOST there.
    ### # Now we haver something that looks like this:
    ### # ['Transcript of a Dictabelt Recordingof a Conversation Between HowardHunt and Charles Colson, November1972', 'COLSON', 'Hello.', 'HUNT', 'Hi.', 'COLSON', "How we doin'?", 'HUNT', 'Well, uh, about as can be expected.  How areyou?']
    ### # 
    ### # And we need to turn this into:
    ### # { 
    ### #   "speaker":"HUNT",
    ### #   "tokens" : ["Well, uh, about as can be expected.","How are you?"]
    ### # }
    ### #
    ### # Go through each list item
    ### # If it's a name,
    ### #   store name as "speaker"
    ### #   store next token as "alltokens"
    ### #   split() on "alltokens" to get your list of "tokens"
    ### #   assemble every person's speaking lines into a single JSON dict 
    ### # 
    ### # Finally, figure out how to append dictionaries in a JSON file









    ### # now we can chop the data up into 
    ### # - header
    ### # - dialogue
    ### # - footer

    ### # then further process each piece.
    ### # further processing means extracting
    ### # and parsing relevant details, and
    ### # putting that all into JSON structure.



    ### # header:
    ### # everything up until the occurrence of the first name
    ### header = data[0:all_indx[0]]

    ### # body:
    ### # everything else
    ### body = data[all_indx[0]:]

    ### # footer:
    ### # there is no footer



    ### # Now turn this into JSON


    ### # Consideration: there are probably multiple formats.
    ### # Take a quick look to determine how they group up.
    ### # Divide them by directory.

