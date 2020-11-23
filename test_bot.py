import praw
import string
import re

#pull bot information from user_info.txt
info = open('user_info.txt', 'r').read().split(',')

reddit = praw.Reddit(user_agent=info[0], client_id=info[1], client_secret=info[2], username=info[3], password=info[4])

i = 0
for submission in reddit.subreddit('all').stream.submissions():

        if str(submission.subreddit)[:2] != 'u_':
                file = open('test_output1.csv', 'a')
                clean_title = "".join([char for char in submission.title if char not in string.punctuation])
                clean_url = "".join([char for char in str(submission.url) if char != ','])
                if(clean_url[4] == 's'):
                        clean_url = clean_url[8:]
                else:
                        clean_url = clean_url[7:]

                split_url = clean_url.split('.')
                if(split_url[0] in ['www']):
                        clean_url = '.'.join(split_url[1:])
                else:
                        clean_url = '.'.join(split_url)
                print(clean_url)
                file.write(str(i) + ',' + str(clean_title) + ',' + str(submission.subreddit) + ',' + str(submission.over_18) + ',' + str(submission.is_self) + ',' + str(clean_url) + '\n')
                file.close()
                
                file = open('subreddit1.csv', 'a')
                file.write(str(i) + ',' + str(submission.subreddit) + '\n')
                file.close()
                i+=1