#!/usr/bin/env python3

from scanner import scanner, download

# Test on scanner.py

# Try getting /a/ catalog as json
catalog_json = scanner.get_catalog_json(a)

# Try getting a list of threads
list_of_threads = scanner.scan_thread("anime", catalog_json)

if list_of_threads is None:
    exit(1)

# try writting a test log file
scanner.add_to_downloaded(".", "log", "139294614")

# test on download.py

# Try getting a web page text
download.load("http://www.4chan.org")
