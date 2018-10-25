import requests
from bs4 import BeautifulSoup
import re
#text=[]
i=''

def striphtml(data):
    p = re.compile(r'<.*?>')
    text=p.sub('', data)
    return text

def filenameexist(filename):
    if not filename:
     return
    else:
     f=open(filename,'w')
     f.write('')
     f.close

def writef(filename, data):
 f = open(filename,'a')
 f.write(data)
 f.close


base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"lxml")
#print soup.p.string
filenameexist('page.txt')

for story_text in soup.findAll(['data-reactid=','p']):
    item=striphtml(str(story_text))
    #text.append(item)
    #text.append('/n')
    #print(text)
    print (item)
    writef('page.txt',item + "\n") 
   
