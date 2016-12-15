from urllib import *
from os.path import basename
import os

base_url='http://nixon.archives.gov'

with open('links.txt','r') as f:
    hrefs = f.readlines()

for href in hrefs:

    print "Retrieving url: "+base_url+href

    filename = '../1primarytexts/pdf/'+basename(href)
    if os.path.exists(filename) is False:
        urlretrieve(base_url+href, filename)

    print "Saved to "+filename
    print "\n"

