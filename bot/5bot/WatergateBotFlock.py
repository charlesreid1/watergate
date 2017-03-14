import rainbowmindmachine as rmm
import logging
from collections import deque
from rainbowmindmachine import QueneauSheep
from rainbowmindmachine.queneau import DialogueAssembler
from random import random


class WatergateSheep(QueneauSheep):

    def populate_queue(self):
        dialogue = DialogueAssembler.loadlines(open(self.params['file']))
        last_speaker = None

        # Deal more elegantly with speakers.
        messages = []
        speakers = []

        #legit_speakers = ['PRESIDENT','EHRLICHMAN','HALDEMANN','KLEINDEIST','HUNT','DEAN','MITCHELL','MCGRUDER','LARUE','COLSON','KISSINGER','FORD']
        legit_speakers = ['COLSON','HUNT','DEAN','PRESIDENT']


        ################################

        # 100-150 messages. no no - moar moar moar
        Nmessages = int(round(20*random()+15))

        # 4-8 speakers
        Npersons  = 4#int(round(3*random()+5))

        N = 0
        while N < Nmessages:

            speaker, tokens = dialogue.assemble(last_speaker)

            z = len(speakers)
            if z < Npersons:
                if speaker in legit_speakers or (random()>0.60):
                    speakers.append(speaker)

            if speaker in speakers:
                last_speaker = speaker
                s = "%s: %s" % (speaker, " ".join(x for x, y in tokens))
                messages.append(s)
                N += 1

        tweet_queue = deque(messages,maxlen=Nmessages)

        return tweet_queue



def setup():
    k = rmm.TxtKeymaker()
    k.make_keys('/home/charles/codes/watergate/bot/5bot/data/')
    
def run():
    sh = rmm.Shepherd('/home/charles/codes/watergate/bot/5bot/keys/',sheep_class=WatergateSheep)

    #sh.perform_pool_action('tweet',{'publish':False})
    sh.perform_pool_action('tweet',{
            'publish' : True,
            'inner_sleep' : 120,
            'outer_sleep' : 1*3600
        })

if __name__=="__main__":
    run()

