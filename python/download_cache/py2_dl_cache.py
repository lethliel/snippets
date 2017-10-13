#!/usr/bin/python

import os.path
import re
import requests
# from urllib.parse import urlparse
from urlparse import urlparse
# from pathlib import Path

# TODO: https://stackoverflow.com/questions/30405867/how-to-get-python-requests-to-trust-a-self-signed-ssl-certificate

# def make_cache_dir(pathname):
#   # https://stackoverflow.com/questions/6004073/how-can-i-create-directories-recursively#6004084
#   path = Path(os.path.dirname(pathname))
#   try:
#     path.mkdir(parents=True) # python 3.5: , exist_ok=True)
#   except FileExistsError:
#     pass
#   return(True)

def cache_me(url):
  try:
    parsed_url=urlparse(url)
    filename = "/tmp/osccache/%s/%s" % (parsed_url.netloc, parsed_url.path)
    if get_cached_or_remote(filename, url):
      print("Cached: %s to %s" % (url, filename))
  except Exception as e:
    print("%s: %s" % (e.__class__, e))

def get_cached_or_remote(filename, url):
  if os.path.exists(filename):
    print("Cache file already exists: %s" % filename)
    return(True)
  r = requests.get(url, stream=True)
  r.raise_for_status()
#  make_cache_dir(filename)
  # write code directly from the requests package documentation
  # only bumped the chunk size
  with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=4096):
      fd.write(chunk)
  return(True)

# fails with 404
# cache_me('https://download.opensuse.org/repositories/openSUSE:/Factory/snapshot/x86_64/attr-2.4.47-7.109.x86_64.rpm')
# working
# cache_me('https://download.opensuse.org/tumbleweed/repo/oss/license.tar.gz')
# requires /etc/hosts entry
# this should fail with "mismatching certificate"
# cache_me('https://downloadoo.nordisch.org/tumbleweed/repo/oss/license.tar.gz')
cache_me('https://download.opensuse.org/tumbleweed/repo/oss/suse/noarch/lua-macros-20170611-1.2.noarch.rpm')
