
# coding: utf-8

# In[1]:

import json
import requests
from github import Github
import mysql.connector
from mysql.connector import errorcode


# In[2]:

access_token='0231643decfea4f7c1d16fdcf893dc6b85592da9'

url="https://api.github.com/repos/torvalds/linux/comments?access_token=0231643decfea4f7c1d16fdcf893dc6b85592da9"
response=requests.get(url)



#print json.dumps(response.json()[0], indent=1)

q1=response.json()[0]
commented_repo="linux"
body=q1["body"]
print q1["user"]["login"]
user=q1["user"]

userid=user["id"]
# In[3]:

config = {
  'user': 'root',
  'password': 'resnick1',
  'host': '127.0.0.1',
  'database': 'UserComments',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


# In[4]:
query = ("SELECT COUNT(*) FROM comments WHERE id=%s")
cursor.execute(query,(userid,))
(res,)=cursor.fetchone()
print 'res is ',res
if res==0:
    add_comment = ("INSERT INTO comments "
                   "(login,id,commented_repo,avatar_url,gravatar_id,followers_url,following_url,gists_url,starred_url,subscriptions_url,organizations_url,repos_url,events_url,received_events_url,type,body) "
                   "VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s)")


    # In[5]:

    cursor.execute(add_comment,(user["login"],user["id"],commented_repo,user["avatar_url"],user["gravatar_id"],user["followers_url"],user["following_url"],user["gists_url"],user["starred_url"],user["subscriptions_url"],user["organizations_url"],user["repos_url"],user["events_url"],user["received_events_url"],user["type"],body))

else:
    new_comment=" #NEWCOMMENT# "+q1["body"]
    update_comment=("UPDATE comments SET body=CONCAT(body,%s) where id = %s")
    cursor.execute(update_comment,(new_comment,userid))


# In[12]:


# In[11]:

for (id,) in cursor:
    print 'id is ',id

cnx.commit()
cursor.close()
cnx.close()

