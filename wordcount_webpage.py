import re
from urllib2 import urlopen
from bs4 import BeautifulSoup
url = 'http://programminghistorian.org/lessons/working-with-web-pages'

soup = BeautifulSoup(urlopen(url), 'html.parser')

soup_str = ''.join(soup.text).encode('utf-8').lower().strip()

words_list = re.findall(r'[A-Za-z]+', soup_str.strip())

words_count = {}

for each in words_list:
    if each in words_count:
        words_count[each] += 1
    else:
        words_count[each] = 1

for d in sorted(words_count, key= words_count.get, reverse=True):
    print d, words_count[d]