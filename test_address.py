#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import urllib
import string
import fileinput
import sys
import csv

def get_address_page(address):
    url = 'http://parasykjiems.lt/pjweb/'
    params = urllib.urlencode({'address_input': address})
    return urllib.urlopen(url, params).read()


def get_page_stats(address, html):
    patterns = ['>Seimo narys <', '>Meras <', '>Seniūnas <', '>Seniūnaitis <']
    result = [address]
    for pat in patterns:
        result.append(string.count(html, pat))
    return result


# main:

adr = 'Gedimino pr. 9, Vilnius'

writer = csv.writer(sys.stdout)

writer.writerow( ['Adresas', 'Seimo narys', 'Meras', 'Seniūnas', 'Seniūnaitis'] )

for adr in fileinput.input():
    adr = adr.strip()
    writer.writerow( get_page_stats(adr, get_address_page(adr)) )
