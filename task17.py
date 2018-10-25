from bs4 import BeautifulSoup
import re
import requests
titles=[]

url='http://nyt.com'
r = requests.get(url)
r_html=r.text

def striphtml(data):
    p = re.compile(r'<.*?>')
    print p.sub('', data)

soup=BeautifulSoup(r_html,"lxml")
for story_heading in soup.findAll(['class="balancedHeadline"','h2']): 
#    print soup.get_text(story_heading)
    titles.append(str(story_heading))
    striphtml(str(story_heading))

#import subprocess
#process = subprocess.call("curl -ikLsv 'https://nytimes.com'| sed 's/,/\n/g'| grep 'promotionalHeadline' | cut -d':' -f2",shell=True)

