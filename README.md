# Watergate

This repository contains some Watergate stuff.

The ultimate goal is to create a whiz-bang tool
that will scrape a website for PDF files,
OCR those PDF files, turn them into JSON,
and feed the whole thing to a leonardr twitterbot.

## Dependencies

### Beautiful Soup

http://www.crummy.com/software/BeautifulSoup/

```
pip install beautifulsoup4
```

### Urllib

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

Most human-intensive step.

Yup. That's it.

## Step 4: Olipy the JSON

This should be sweet and simple.

