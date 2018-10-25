import re
import requests
import subprocess
import os
from bs4 import BeautifulSoup
x=''
item=''

def inputname():
 x= str(raw_input("Enter filename to save : "))
 x = os.getcwd()+"/"+x
 #print(x)
 download(x)

def striphtml(x,data):
    p = re.compile(r'<.*?>')
    text=p.sub('', data)
    writef(x,text)

def writef(filename, data):
 #print(filename)   
 f = open(filename,'a')
 f.write(data)
 f.close


def download(x):
 base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
 r = requests.get(base_url)
 soup = BeautifulSoup(r.text,"lxml")
 for story_text in soup.findAll(['data-reactid=','p']):
  story_text=str(story_text)
  item==striphtml(x,story_text)
  #print (item)
  writef(x,str(item) + "\n") 

inputname()
