
# coding: utf-8

# In[1]:

import json
import requests
from github import Github
import mysql.connector
from mysql.connector import errorcode
from os.path import expanduser
home=expanduser('~')
print 'hi'


# In[2]:

f=open(home+'/coursework/github token')
access_token=f.readline()

def getResponse(url):
    response=requests.get(url)
    d=response.headers.items()
    for (k,v) in response.headers.items():
        if k=="link":
            link=v
    return response.status_code,link,response.json()

url1="https://api.github.com/users/leeight/followers"
url1="https://api.github.com/users/robbenmu"
url=url1+"?access_token="+access_token
print url ,' : done '
response=requests.get(url)

for (k,v) in response.headers.items():
    print  k,' : ',v

        
print '\n\n\n\n'
print 'the number of followers is ',len(response.json())

'''
(code,link,response)=getResponse(url)
#print 'link are ',link
while(1):
    if code==200:
        links=link.split(';')
        link1=links[0]
        #print 'link1 is ',link1,'\n'
        link2=links[1].split(',')
        #print ' 1 link2 is ',link2

        link2=link2[1]
        link2=link2.rstrip()
        link2=link2.lstrip()
        #print '2 link2 is \n',link2
        link1=link1[1:-1]
        link2=link2[1:-1]
        print 'link1 is ',link1 ,' link2 is ',link2
        if link1==link2:
            break;
        (code,link,response)=getResponse(link1)
        print '\n\n'
    #while()


'''





