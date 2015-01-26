import sys
import PyPDF2
import os
from os.path import splitext
from os.path import basename

"""
via http://stackoverflow.com/questions/15583535/how-to-extract-text-from-a-pdf-file-in-python
"""

def convertPdf2String(path):
    """
    Turn a PDF file into a string
    """
    content = ""
    pdf = PyPDF2.PdfFileReader(file(path, "rb"))
    for i in range(0, pdf.getNumPages()):
        content += pdf.getPage(i).extractText() + " \n"
        content = " ".join(content.replace(u"\xa0", u" ").strip().split())
    return content

datdir = '../1primarytexts/'

# get list of pdf files
filenames = []
for f in os.listdir(datdir):
    if f.endswith(".pdf"):
        filenames.append( basename( splitext(f)[0] ) )

print filenames

for filename in filenames:
    print "Extracting text from "+filename+".pdf to "+filename+".txt ..."
    try:
        f = open(datdir+filename+'.txt','w+')
        f.write(convertPdf2String(datdir+filename+'.pdf').encode("ascii","xmlcharrefreplace"))
        f.close()
        print "Done."
        print "\n"
    except:
        print "Error encountered."
        print "\n"


