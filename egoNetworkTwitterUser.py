# --------------------------------------------- #
# --- prepared by: Hend Alrasheed - halrasheed@ksu.edu.sa --- #
# --- Oct 2019 --- #
# --- The code returns the ego network of a given twitter user. The network will 
# --- be returned in a text file (directed edge list) format.
# --------------------------------------------- #

import tweepy
import time
import sys
import os
import unicodedata

#----------------------------------------------------


def load_first_degree_followers(user):

    ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name=user).pages():
       ids.extend(page)
       time.sleep(60)

    for i in ids:
        f.write(str(i) + "  " + str(user_id) + "\n")

    print 'Done with the 1st degree followers'

    return ids

#----------------------------------------------------

def load_first_degree_friends(user):

    ids = []
    for page in tweepy.Cursor(api.friends_ids, screen_name=user).pages():
       ids.extend(page)
       time.sleep(60)

    for i in ids:
        f.write(str(user_id) + "  " + str(i) + "\n")

    print 'Done with the 1st degree freinds'

    return ids

#----------------------------------------------------

def load_second_degree_followers(users):

    ids = []
    for user in users:
        try:
            if api.get_user(user).protected == False:
               ids = []
               for page in tweepy.Cursor(api.followers_ids, id=user).pages():
                   ids.extend(page)
                   time.sleep(60)

               for i in ids:
                   f.write(str(i) + "  " + str(user) + "\n")

        except Exception:
             pass 

    print 'Done with the 2nd degree followers'
    
#----------------------------------------------------

def load_second_degree_friends(users):

    ids = []
    for user in users:
        try:
            if api.get_user(user).protected == False:         
               ids = []
               for page in tweepy.Cursor(api.friends_ids, id=user).pages():
                   ids.extend(page)
                   time.sleep(60)

               for i in ids:
                   f.write(str(user) + "  " + str(i) + "\n")
                  
        except Exception:
             pass            

    print 'Done with the 2nd degree friends'
    

#----------------------------------------------------

CONSUMER_KEY    = ''
CONSUMER_SECRET = ''
ACCESS_KEY      = ''
ACCESS_SECRET   = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

username = sys.argv[1]
user = api.get_user(username) 
user_id = user.id
print user.id
f  = open(username+'-ego-network.txt', 'w')

print 'Retrieving user data...'
first_degree_followers = load_first_degree_followers(username)
first_degree_friends   = load_first_degree_friends(username)
load_second_degree_followers(first_degree_followers)
load_second_degree_friends(first_degree_friends)


f.close()
print 'Ego network file is ready...'
