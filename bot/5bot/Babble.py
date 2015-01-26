"""
Make some Apollo Ipsum...
"""
from queneau import DialogueAssembler

def main():

    ipsum_file = "apollo11_ipsum.txt"
    data_file = "data/apollo_11.txt"
    
    generate_ipsum(ipsum_file,data_file,N=150)


def generate_ipsum(ipsum_file,data_file,N=100):

    dialogue = DialogueAssembler.loadlines(open(data_file))
    
    last_speaker = None
    
    with open(ipsum_file,"w") as f:
    
        # Bursts of conversation of N messages
        for N_ in range(N):
            """
            expand_pattern(self, pattern, length)
                Decode a short string representing a family of Queneau assembly.
           
                Some common families, expanded to length 5:
           
                "0." -> 0, 1, 2, 3, 4
                "0.l" -> 0, 1, 2, 3, last
                "f.l" -> first, middle, middle, middle, last
                "f." -> first, middle, middle, middle, last
                "." -> first, middle, middle, middle, last
           
                Some less common families:
           
                "011." -> 0, 1, 1, 2, 3
                "011.l" -> 0, 1, 1, 2, last
                "0f1fl" -> 0, 0, 1, 0, last
                "f.f" -> first, middle, middle, middle, first
                "l.f" -> last, middle, middle, middle, first
                "m.l" -> middle, middle, middle, middle, last
            """
        
            # Inner loop: messages spaced with short intervals.
            speaker, tokens = dialogue.assemble(last_speaker,pattern="0.")
            last_speaker = speaker
            s = "%s: %s" % (speaker, " ".join(x for x, y in tokens))
        
            #f.write(s.decode('utf-8'))
            f.write(s)
            f.write('\n\n')

if __name__=="__main__":
    main()
