# Watergate

This repository contains scripts for text processing related to publicly-released Watergate transcripts.

It contains Python scripts that will scrape a website for PDF files, download those PDF files, turn them
into text, process the text, and output a JSON data structure.

As a proof-of-concept this JSON structure will be hooked up to Olipy to create a twitterbot agent of chaos.

## Dependencies

### Beautiful Soup

This is used to process HTML tags. Link: http://www.crummy.com/software/BeautifulSoup/

```
pip install beautifulsoup4
```

### Urllib

This is used to download the PDF files.

```
pip install urllib
```

## Step 1: Finding Primary Text Sources

I'm using the following websites for PDF files of transcripts:

http://nixon.archives.gov/forresearchers/find/tapes/watergate/trial/transcripts.php

http://nixon.archives.gov/forresearchers/find/tapes/watergate/wspf/transcripts.php

## Step 2: Scraping PDFs

Scrape HTML, look for links to PDFs, create list, download each item in list

BeautifulSoup to parse HTML for links, Urllib to download PDF links.

## Step 3: Extract PDF Text to JSON

This uses a Python PDF utility to turn the PDF into text, which works fairly well.

This text is further processed into JSON pieces.

## Step 4: Olipy the JSON

This comes at the end, but it should be really easy. Proof: http://charlesmartinreid.com/wiki/Apollo11Junk

