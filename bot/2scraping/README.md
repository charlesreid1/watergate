# Step 2: Scraping PDFs

This is straightforward: we're looking for all PDF links with the link text "Transcript" 
on the Watergate transcript pages.

We then want to download those files.

This uses BeautifulSoup to break apart the tag hierarchy.

This uses urllib to download the PDF links.


