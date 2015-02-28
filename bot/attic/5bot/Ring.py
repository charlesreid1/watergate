import urlparse
import oauth2 as oauth
import os
import time
import re
import simplejson as json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import httplib

from apikeys import *

"""
Ring

Loads a set of JSON keys into memory,
performs collective account actions on bot flock accounts.

Valid parameters accepted by Twitter API are listed here:
    https://dev.twitter.com/rest/reference/post/account/update_profile


===============
Notes:

The key to getting this to work was here:
    http://stackoverflow.com/questions/680305/using-multipartposthandler-to-post-form-data-with-python

This page:
    http://stackoverflow.com/questions/14836956/how-to-get-user-image-with-twitter-api-1-1
shows a get request.
I think you gotta combine get and post methods.
    api.twitter.com/api/something.json/url?screen_name=charlesreid1

Close. You have to sign a POST request,
then turn it into a regular GET request.
(Apparently...?)

gist:
    https://gist.github.com/velocityzen/1242662
SO thread:
    http://stackoverflow.com/questions/6924569/doing-a-file-upload-with-python-oauth2

This SO thread did it:
    http://stackoverflow.com/questions/12977604/how-do-i-send-a-post-using-2-legged-oauth2-in-python

Boom.
Twitter expects body to be a JSON
containing whatever parameters are listed 
on the Twitter API documentation.
"""

# Register the streaming http handlers with urllib2
# http://stackoverflow.com/questions/680305/using-multipartposthandler-to-post-form-data-with-python
register_openers()
            


def main():
    r = Ring('keys/')
    #change_milton_bios(r)
    #change_milton_urls(r)
    #change_milton_colors(r)
    #change_milton_images(r)
    r.change_profile()






class Ring(object):

    def __init__(self,keys_dir):

        self.keys_dir = keys_dir

        raw_files = os.listdir(keys_dir)

        # all_json is the list of all 
        # JSON files from which we'll
        # grab key info (to perform
        # group operations)
        all_json = []
        for rfile in raw_files:
            if rfile[-5::]=='.json':
                all_json.append(rfile)

        self.all_json = all_json
        
        # all_keys is a list of dictionaries
        # that contain the bundle of bot info
        # stored in each JSON file
        all_keys = []
        for jsonf in all_json:
            full_jsonf = keys_dir + jsonf
            print "Loading key in json file "+full_jsonf
            with open(full_jsonf, "r") as f:
                all_keys.append( json.load(f) )

        self.all_keys = all_keys


    def get_keys(self):
        """
        Returns a list of dictionaries
        containing key info for each bot
        """
        return self.all_keys


    def change_bot_url(self,urls):
        """
        url should be a dictionary:
        url[username] = "http://url"
        """
        for key_dictionary in self.all_keys:

            handle = key_dictionary['screen_name']
            bot_url = urls[handle]

            # -----------------------------------------
            # Set the API endpoint 
            url = "https://api.twitter.com/1.1/account/update_profile.json"

            import urllib

            token = oauth.Token(key = key_dictionary['oauth_token'], 
                             secret = key_dictionary['oauth_token_secret'])
            consumer = oauth.Consumer(key = key_dictionary['consumer_token'], 
                                   secret = key_dictionary['consumer_token_secret'])
            client = oauth.Client(consumer,token)
            resp, content = client.request(
                    url,
                    method = "POST",
                    body=urllib.urlencode({'url': bot_url}),
                    headers=None
                    )
            
            print content



    def change_profile(self):

        for key_dictionary in self.all_keys:

            ########################################
            # This page:
            # http://stackoverflow.com/questions/14836956/how-to-get-user-image-with-twitter-api-1-1
            # shows a get request.
            # I think you gotta combine get and post methods.
            # api.twitter.com/api/something.json/url?screen_name=charlesreid1
            #
            #
            # Close. You have to sign a POST request,
            # then turn it into a regular GET request.
            # (Apparently...?)
            # 
            # This gist:
            # https://gist.github.com/velocityzen/1242662
            # This SO thread:
            # http://stackoverflow.com/questions/6924569/doing-a-file-upload-with-python-oauth2
            #
            # This SO thread did it:
            # http://stackoverflow.com/questions/12977604/how-do-i-send-a-post-using-2-legged-oauth2-in-python
            # Boom.
            # Twitter expects body to be a JSON
            # containing whatever parameters are listed 
            # on the Twitter API documentation.
            ########################################

            handle = key_dictionary['screen_name']

            descr2title = {}
            descr2title['ThisIsWatergate'] = 'The tougher it gets, the cooler I get.'

            the_url = 'http://charlesreid1.github.io/watergate'

            # -------------------

            # Set the API endpoint 
            url = "https://api.twitter.com/1.1/account/update_profile.json"

            import urllib

            token = oauth.Token(key = key_dictionary['oauth_token'], 
                             secret = key_dictionary['oauth_token_secret'])
            consumer = oauth.Consumer(key = key_dictionary['consumer_token'], 
                                   secret = key_dictionary['consumer_token_secret'])
            client = oauth.Client(consumer,token)
            resp, content = client.request(
                    url,
                    method = "POST",
                    body=urllib.urlencode({'url': the_url,
                                           'description': descr2title[handle]}),
                    headers=None
                    )
            
            print content





    def change_bot_bio(self,bios):
        """
        bio should be a dictionary:
        bio[username] = "bios"
        """
        for key_dictionary in self.all_keys:

            handle = key_dictionary['screen_name']
            bot_bio = bios[handle]

            # -----------------------------------------
            # Set the API endpoint 
            url = "https://api.twitter.com/1.1/account/update_profile.json"

            import urllib

            token = oauth.Token(key = key_dictionary['oauth_token'], 
                             secret = key_dictionary['oauth_token_secret'])
            consumer = oauth.Consumer(key = key_dictionary['consumer_token'], 
                                   secret = key_dictionary['consumer_token_secret'])
            client = oauth.Client(consumer,token)
            resp, content = client.request(
                    url,
                    method = "POST",
                    body=urllib.urlencode({'description': bot_bio}),
                    headers=None
                    )
            
            print content


    def change_bot_colors(self,background_rgbcodes=None,link_rgbcodes=None):
        """
        {background,link}_rgbcodes should be a dictionary:
        rgbcodes[username] = "RRGGBB"
        """
        for key_dictionary in self.all_keys:

            handle = key_dictionary['screen_name']

            if background_rgbcodes <> None:
                bot_bkg_rgb = background_rgbcodes[handle]
            else:
                # default
                bot_bkg_rgb = "3D3D3D"

            if link_rgbcodes <> None:
                bot_lnk_rgb = link_rgbcodes[handle]
            else:
                # default
                ## twitter blue:
                #bot_lnk_rgb = "4099FF"
                # navy blue:
                bot_lnk_rgb = "000080"

            # -----------------------------------------
            # Set the API endpoint 
            url = "https://api.twitter.com/1.1/account/update_profile_colors.json"

            import urllib

            token = oauth.Token(key = key_dictionary['oauth_token'], 
                             secret = key_dictionary['oauth_token_secret'])
            consumer = oauth.Consumer(key = key_dictionary['consumer_token'], 
                                   secret = key_dictionary['consumer_token_secret'])
            client = oauth.Client(consumer,token)
            resp, content = client.request(
                    url,
                    method = "POST",
                    body=urllib.urlencode({ 'profile_background_color': bot_bkg_rgb,
                                            'profile_link_color': bot_lnk_rgb }),
                    headers=None
                    )
            
            print content






    def change_bot_img(self,img_files):
        """
        img_files should be a dictionary:
        img_files[username] = "img/file.jpg"
        """
        for key_dictionary in self.all_keys:

            handle = key_dictionary['screen_name']

            img_file = img_files[handle]

            # -----------------------------------------
            # Set the API endpoint 
            domain = "https://api.twitter.com"
            url = domain+"/1.1/account/update_profile_image.json"

            import urllib

            token = oauth.Token(key = key_dictionary['oauth_token'], 
                             secret = key_dictionary['oauth_token_secret'])
            consumer = oauth.Consumer(key = key_dictionary['consumer_token'], 
                                   secret = key_dictionary['consumer_token_secret'])
            client = oauth.Client(consumer,token)

            req = oauth.Request.from_consumer_and_token(
                    consumer, 
                    token=token, 
                    http_url=url,
                    parameters=None, 
                    http_method="POST")
            req.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)


            # Generate multipart data and headers from content
            datagen, headers = multipart_encode({'image': open(img_file,'rb')})


            # Append OAuth Authorization headers to generated headers
            headers.update(req.to_header())

            # Body to string
            body = "".join(datagen)

            # Create the Request object
            request = urllib2.Request(url, datagen, headers)
            print urllib2.urlopen(request).read()



############################################################################
############################################################################


def change_milton_bios(r):
    prefix = 'Tweeting John Milton\'s Paradise Lost Book '
    suffix = ' in perpetuity'
    bio = {}
    for i in range(1,13):
        handle = 'milton_book'+str(i)
        bio[handle] = prefix+str(i)+suffix
    r.change_bot_bio(bio)

def change_milton_urls(r):
    github_url = 'https://github.com/charlesreid1/milton'
    url = {}
    for i in range(1,13):
        handle = 'milton_book'+str(i)
        url[handle] = github_url
    r.change_bot_url(url)

def change_milton_colors(r):
    r.change_bot_colors()

def change_milton_images(r):
    url = {}
    for i in range(1,13):
        handle = 'milton_book'+str(i)
        img_file = 'img/book'+str(i)+'.jpg'
        url[handle] = img_file
    r.change_bot_img(url)

if __name__=="__main__":
    main()

