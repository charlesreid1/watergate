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
        pagecontent = pdf.getPage(i).extractText().replace(u"\xa0",u" ").strip().split()
        pagecontent += ["\n"]
        content = " ".join(pagecontent)
    return content

datdir = '../1primarytexts/pdf/'
txtdir = '../1primarytexts/txt/'

# get list of pdf files
filenames = []
for f in os.listdir(datdir):
    if f.endswith(".pdf"):
        filenames.append( basename( splitext(f)[0] ) )


for filename in filenames:
    print "Extracting text from "+datdir+filename+".pdf to "+txtdir+filename+".txt ..."
    try:
        f = open(txtdir+filename+'.txt','w+')
        contents = convertPdf2String(datdir+filename+'.pdf').encode("ascii","xmlcharrefreplace") 
        f.write( contents )
        f.close()
        print "Done."
        print "\n"
    except IOError:
        print "IO error encountered. Continuing..."
        print "\n"
    except TypeError:
        print "Weird error encountered."
        print datdir+filename+'.pdf'
        print "Continuing..."
        print "\n"


