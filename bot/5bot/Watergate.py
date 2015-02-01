from Shepherd import *

def the_real_mccoy():
    """
    This is it. The Real McCoy.
    """
    s = Shepherd()
    s.setup('keys/',
            line_interval = 140,
            total_interval = 14400 ) # 4 hrs

    # for test_tweet:
            #line_interval = 1, 
            #total_interval = 15 ) 
    s.loop()

if __name__=="__main__":
    the_real_mccoy()


