from Shepherd import *

def jonestown():
    """
    Every bot destroys its own history
    """
    s = Shepherd()
    s.setup('keys/')
    s.jonestown()

if __name__=="__main__":
    jonestown()
