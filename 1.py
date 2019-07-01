#!/usr/bin/python3

import urllib.parse

a = 'https://somewhere.earningmoney.com'.replace('.', '_')
b = urllib.parse.urlparse(a)
print((b.hostname))

if a != '':
  host_name_from_db = 'https://192.168.34.5'.replace('.', '_')
  replased_hostname = urllib.parse.urlparse(host_name_from_db)
  print((replased_hostname.hostname))
