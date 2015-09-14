import urllib
import BeautifulSoup as  b

content  = urllib.urlopen('http://www.parsclick.net').read()

soup = b.BeautifulSoup(content)
print (soup.body
print('\r\n')
print(soup.div['clear'])
#print soup.find('class=clear')
print(soup.find('nav', id="site-navigation"))

