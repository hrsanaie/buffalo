__author__ = 'root'

import urllib.request as ur  # retreive the content of webpage

myurl = ur.urlopen("http://pentesterschool.ir")  # just retreive webpage content
#print(myurl.info())  # print head of webpage
contents = myurl.readlines()
for row in contents:
    print("%s" % row)


####################333

# retrevice webpage content and save into the file
ur.urlretrieve("http://securityweekly.com", filename="fucking-securityweekly.dat")
myurl.close()


################33

# for present url content as plaintext (dont like HTML format)
import html5lib  # for HTML parsing
import formatter  # for set the content as plaintext
import sys  # for standard input/output format

myurl = ur.urlopen("http://google.com")
contents = myurl.readlines()
myurl.close()

fmt = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))  # set plaintext format
convertToPlainText = html5lib.parse(fmt)  # for configure parser with this format
convertToPlainText.feed(contents) # feed parser with my webpage content
convertToPlainText.close()

