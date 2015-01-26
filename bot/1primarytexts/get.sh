#!/bin/sh

wget http://nixon.archives.gov/forresearchers/find/tapes/watergate/trial/transcripts.php 
sed -e 's///' transcripts.php > trial.html
rm transcripts.php

wget http://nixon.archives.gov/forresearchers/find/tapes/watergate/wspf/transcripts.php 
sed -e 's///' transcripts.php > wspf.html
rm transcripts.php

