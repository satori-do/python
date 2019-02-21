#! /usr/bin/python

# from urlparse import urlparse
import urlparse
# zzz = self._query("USE dashboard; SELECT value FROM config_variable WHERE name='HOSTNAME';")
# a = 'https://192.168.34.5'.replace('.', '_')
a = 'https://stg55.metricinsights.com'.replace('.', '_')
#c = '(('https://192.168.33.19',),)'.replace('.', '_')
b = urlparse.urlparse(a)
# .replace(".", "_")
# a.replace('.', '_')
# string.replace(s, 'est', '')
# a = 'https://stg55.metricinsights.com' -> stg55_metricinsight_com
# a = ''
# if a == '': a = 'socket.gethostname()'
# self.db_exists('dashboard')
print b.hostname
if a != '':
  host_name_from_db = 'https://192.168.34.5'.replace('.', '_')
  replased_hostname = urlparse.urlparse(host_name_from_db)
  print replased_hostname.hostname
# socket.gethostname() = replased_hostname.hostname
