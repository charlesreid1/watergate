from urllib import *
from os.path import basename
from random import random
import os, re, time

base_url='http://nixon.archives.gov'

with open('links.txt','r') as f:
    hrefs = f.readlines()


for href in hrefs:

    href = re.sub('\n','',href)

    print "Retrieving url: "+base_url+href

    filename = '../1primarytexts/pdf/'+basename(href).strip()

    if os.path.exists(filename) is False:

        
        maxtries = 2



        connected = False
        tries = 0
        while( not connected and tries<=maxtries):

            try:
                urlretrieve( base_url+href, filename )
            except IOError:
                print "Failed - trying again in 1 second..."
                time.sleep(5)
                tries += 1

        if(not connected):
            print "Giving up on %s"%(base_url+href)


    print "Saved to "+filename
    print "\n"

