# Author: Jack Billimack
# Gather comments from Youtube Video 
# Date: 10/03/2020
# mail: ~~~
# github:~~~
try:
    from config import api_key
except:
    api_key = "XXX"

comment_url = 'https://www.googleapis.com/youtube/v3/commentThreads'

import requests
import pandas as pd
import json

# video_id = ' UI1vHrMNp0w'#'yvGrsBqe-KQ'

def make_comment_dataframe(video_id):
    '''
    Make a dataframe of all comments for a given video.

    video_id = the video id of a youtube video that you would like comments information about.
    '''
    request_url = comment_url+'?key='+api_key+'&textFormat=plainText&part=snippet&videoId='+video_id +'&maxResults=100'
    comment_df = []
   
    # First request
    r = requests.get(request_url)
    json_data = r.json()                                                                                                
    json_df = pd.DataFrame(json_data["items"])
    comments = pd.json_normalize(json_df['snippet'])
    comment_df.append(comments)
    nextPageToken = json_data.get("nextPageToken")

    # Retrieve all comments until no additional pagination exists
    while nextPageToken:
        r = requests.get(request_url+"&pageToken="+nextPageToken)
        json_data = r.json()
        json_df = pd.DataFrame(json_data["items"])
        comments = pd.json_normalize(json_df['snippet'])
        comment_df.append(comments)
        nextPageToken = json_data.get("nextPageToken")

    comment_df = pd.concat(comment_df)
    return comment_df

#comment_df = make_comment_dataframe(video_id)

# EXPORT
#comment_df.to_csv('\\PATH\\TO\\YoutubeCommentors\\data\\comment_test.csv', index = True, header = True, encoding = 'utf-8')