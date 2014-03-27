# Watergate

This repository contains some Watergate stuff.

The ultimate goal is to create a whiz-bang tool
that will scrape a website for PDF files,
OCR those PDF files, turn them into JSON,
and feed the whole thing to a leonardr twitterbot.

## Dependencies

Beautiful Soup:

http://www.crummy.com/software/BeautifulSoup/

## Step 1: Finding Primary Text Sources

I'm using the following websites for PDF files of transcripts:

http://nixon.archives.gov/forresearchers/find/tapes/watergate/trial/transcripts.php

http://nixon.archives.gov/forresearchers/find/tapes/watergate/wspf/transcripts.php

## Step 2: Scraping PDFs

Scrape HTML, look for links to PDFs, create list, download each item in list

## Step 3: OCR Scan PDFs to Tokenizable Text

Most human-intensive step.

## Step 4: Tokenize to JSON

Yup. That's it.

## Step 5: Olipy the JSON

This should be sweet and simple.

