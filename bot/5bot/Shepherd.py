import time
import os
import re
import json

from Keymaker import *
from Sheep import *


def runsheep(sheeeep):
    """
    This function is run by the thread pool.
    This is where the magic happens. (Kind of.)
    """
    sheeeep.loop()




class Shepherd(object):
    """
    Startup:
        User invokes Keymaker 
        Keymaker generates an oauth token and link
        User visits link while logged in 
        User grants permission to app and gets PIN
        User gives PIN to Keymaker
        Keymaker generates authorization tokens for API
        Keymaker dumps bundle into JSON file - 1 JSON per sheep 
            - auth key, auth token
            - user id, user handle
            - file

    Loop:
        Shepherd loops through the flock
        Tell sheep to tweet
    """
    def __init__(self):
        self.all_json = []
        self.all_sheep = []



    def setup(self,json_key_dir,line_interval=30,total_interval=(1.5*3600)):
        """
        Assume keys have been created
        """
        self.line_interval = line_interval
        self.total_interval = total_interval

        raw_files = os.listdir(json_key_dir) 
        for rfile in raw_files:
            if rfile[-5:] == '.json':
                full_filename = re.sub('//','/',json_key_dir + '/' + rfile)
                self.all_json.append(full_filename)

        for jsonf in self.all_json:
            print "Making Sheep for file "+jsonf
            mysheep = Sheep(jsonf,
                        line_interval=self.line_interval,
                        total_interval=self.total_interval)
            self.all_sheep.append(mysheep)


    def loop(self):
        """
        This is what the Shepherd does...
        forever
        """
        try:
            pool = ThreadPool(len(self.all_sheep))
        except ValueError:
            # no keys found
            raise Exception("Error: did not find any keys, so could not create any Sheep.")

        results = pool.map(runsheep,self.all_sheep)



    def jonestown(self):
        """
        All of our sheep will undergo a mass collective 
        history wipe
        """
        for sheep in self.all_sheep:
            print "Performing a lobotomy for sheep "+sheep.params['screen_name']
            sheep.lobotomy()

