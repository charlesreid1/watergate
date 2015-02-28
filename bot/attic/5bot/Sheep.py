from apikeys import *

import twitter
import time
import simplejson as json
from numpy.random import rand

from queneau import DialogueAssembler

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 

"""
Uses bear's python-twitter library from Github
(official version of what was the Google Code python-twitter):
https://github.com/bear/python-twitter
"""

class SpecialException(Exception):
    pass

class Sheep(object):
    """
    Sheep does three things:
    - communicates with twitter api
    - tweets
    - keeps track of age/# cycles
    """
    def __init__(self,json_file,line_interval,total_interval):

        self.line_interval = line_interval
        self.total_interval = total_interval

        # sheep require a JSON with keys
        print json_file
        with open(json_file, "r") as f:
            self.params = json.load(f)

        # perform some check here
        # to make sure this is valid JSON

        # self.params keys:
        # - oauth_token_secret
        # - oauth_token
        # - user_id
        # - screen_name
        # - consumer_token_secret
        # - consumer_token
        # - myfile

        # sheep interface with twitter
        self.setup_api()

        # sheep has dialogue generator (brain)
        self.dialogue = DialogueAssembler.loadlines(open(self.params['file']))
        self.last_speaker = None

        # sheep can sleep
        self.sleeping = False

        # tot tweet tracker for total lifetime
        # mod tweet tracker for mod N (N = number of lines, which changes with time)
        self.tot_tweet_tracker = 0
        self.mod_tweet_tracker = 0


    def setup_api(self):
        """
        Create Twitter API instance from our input params
        """
        print "Setting up API for bot "+self.params['screen_name']
        self.api = twitter.Api( consumer_key        = self.params['consumer_token'],
                                consumer_secret     = self.params['consumer_token_secret'],
                                access_token_key    = self.params['oauth_token'],
                                access_token_secret = self.params['oauth_token_secret'])



    def memorize(self):
        """
        Memorize a file
        (i.e. read it into list called memory)
        """
        pass



    def loop(self):
        """
        Do this forever
        """
        short = self.line_interval 
        loong = self.total_interval
        while True:


           #########################
           # For the Watergate bot,
           # to create a conversation,
           # we'll want to pick a few speakers
           # and discard all dialogue where
           # those speakers are not present.
           #
           # We can do that here, in the outer loop
           # phone conversations can potentially be 
           # very long. 
           # 
           # For first pass, make this 
           # a perpetual conversation among
           # Nixon, Erlichman, and Haldeman.
           ########################



            #try:

            # Outer loop: bursts of conversation of N messages, 
            # spaced with long intervals.
            Nmessages = int(round(30*rand()+20))
            for N in range(Nmessages):
                print "Doing",N,"of",Nmessages,"messages"

                speaker = ''
                #while speaker not in ['HALDEMAN','EHRLICHMAN','PRESIDENT','NIXON']:
                while speaker not in ['DEAN','PRESIDENT','NIXON']:
                    # Inner loop: messages spaced with short intervals.
                    speaker, tokens = self.dialogue.assemble(self.last_speaker)
                    self.last_speaker = speaker
                    s = "%s: %s" % (speaker, " ".join(x for x, y in tokens))

                #self.test_tweet(s)
                self.tweet(s)

                time.sleep( short*rand() )

            print "\n[...]\n"
            time.sleep( loong*rand() )

            #except:
            #    print "Uh oh! Sheep "+self.params['screen_name']+" ran into a problem."
            #    time.sleep(1000)



    def sleep(self):
        """
        Take a nap
        """
        self.sleeping = True

        # If we've finished the file, longer wait.
        # If we're just between lines, shorter wait.

        if (self.mod_tweet_tracker == 0 and self.tot_tweet_tracker > 0):
            time.sleep(self.total_interval)

        else:
            time.sleep(self.line_interval)

        self.sleeping = False





    def test_tweet(self,txt):
        """
        Tweet hello world + a random favorite number
        """
        #txt = "Hello world! My favorite number is %d"%( round(1000*rand()) )
        #self.tweet(txt)
        print txt



    def tweet(self,txt):
        """
        Really tweet!
        """
        #if self.params['screen_name']=='gbf_supermarket':
        #    print self.params['screen_name']
        #    print txt
        #    print
        try:
            # tweet:
            stats = self.api.PostUpdates(txt)

            # everything else:
            for stat in stats:
                print "[Bot "+self.params['screen_name']+"]: "+stat.text

        except twitter.TwitterError as e:
            if e.message[0]['code'] == 185:
                print "[Bot "+self.params['screen_name']+"] Twitter error: Daily message limit reached"
            elif e.message[0]['code'] == 187:
                print "[Bot "+self.params['screen_name']+"] Twitter error: Duplicate error"
            else:
                print "[Bot "+self.params['screen_name']+"] Twitter error"
                print e.message

        self.increment_tweet_counters()
        self.check_age()



    def increment_tweet_counters(self):
        """
        Increment tweet counters by 1
        """
        self.mod_tweet_tracker += 1
        self.tot_tweet_tracker += 1



    def check_age(self):
        """
        Figure out if we've finished tweeting our file
        """
        pass




    def lobotomy(self):
        """
        Sheep can delete their whole history and pretend like
        none of this ever happened. 

        Deletes every tweet.
        """
        for j in self.api.GetUserTimeline(self.params['screen_name'],count=100):
            print "Destroying status:"
            print j.text
            self.api.DestroyStatus( j.id )
        self.mod_tweet_tracker = 0
        self.tot_tweet_tracker = 0

