from Shepherd import *

def make_keys():
    """
    This goes through each file
    and asks, one by one, if you want to make a key for it.
    Then 'keys/' is populated.
    """
    keymaker = Keymaker()
    keymaker.make_keys('data/')

if __name__=="__main__":
    make_keys()

