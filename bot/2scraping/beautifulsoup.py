from bs4 import BeautifulSoup
from urllib import *
from os.path import basename


html_files = ['trial.html','wspf.html']
base_url='http://nixon.archives.gov'

full_html_files = ['../1primarytexts/'+html_file for html_file in html_files]

hrefs=[]
    
for html_file in full_html_files:

    soup = BeautifulSoup(open(html_file))
    
    for link in soup.find_all('a'):
        href = link.get('href')
        try:
            ext = href[-4:]
            if ext == u'.pdf' and basename(href) != 'guide.pdf':
                hrefs.append(href)
        except:
            pass

for href in hrefs:

    print "Retrieving url: "+base_url+href

    filename = '../1primarytexts/'+basename(href)
    urlretrieve(base_url+href, filename)

    print "Saved to "+filename
    print "\n"

