__author__ = 'root'
import sys , urllib , os
import BeautifulSoup as b
os.system('clear')
req = urllib.urlopen('http://jadi.net').read()
soup = b.BeautifulSoup(req)
print(soup.find('nav', id="site-navigation"))
#print(soup.prettify())