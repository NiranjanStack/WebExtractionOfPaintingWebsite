import urllib
from lxml import etree
#from datetime import datetime
#import pytz
import sys

#webpage_link.txt contains the links from which meta tag contents are to be retrieved
#open the file and read each link
f=open('webpage_link.txt',"r")
lines=f.readlines()

#Append output to file
sys.stdout=open("output.txt","w")

#read the meta tags from each link
for i in lines:
    readLink=urllib.urlopen(i).read()
    tree = etree.HTML(readLink)

    #get eta tag contents using xpath
    if tree.xpath( "//meta[@property='bt:subject']" ) and tree.xpath( "//meta[@property='og:title']" ) :
        subject=(tree.xpath( "//meta[@property='bt:subject']" )[0].get("content"))
        title=(tree.xpath( "//meta[@property='og:title']" )[0].get("content"))
        author,name=title.split(';')
        print(author,subject,name)
		
