import requests
import pandas as pd
import json
try:
    from config import api_key
except:
    api_key = "XXX"


def make_channel_videos_dataframe(channel_id):
    '''
    Make a DataFrame of information relating to a given channel.

    channel_id = The channel id of the channel you would like to collect information about.
    '''
    channel_url = 'https://www.googleapis.com/youtube/v3/search?key='+api_key+'&channelId='+channel_id+'&part=snippet,id&order=date&maxResults=50'
    channel_videos_df = []
   
    # First request
    r = requests.get(channel_url)  # request_url
    json_data = r.json()
    json_df = pd.DataFrame(json_data["items"])
    try:
        id = pd.json_normalize(json_df['id'])
        snippet = pd.json_normalize(json_df['snippet'])
    except KeyError:
        pass
    try:
        channel_videos = id.join(snippet, how='inner')
    except ValueError:
        pass     
    channel_videos_df.append(channel_videos)
    nextPageToken = json_data.get("nextPageToken")

    while nextPageToken:
        json_df = pd.DataFrame(json_data["items"])
        r = requests.get(channel_url+"&pageToken="+nextPageToken)
        json_data = r.json()
        try:
            id = pd.json_normalize(json_df['id'])
            snippet = pd.json_normalize(json_df['snippet'])
        except KeyError:
            break
        try:
            channel_videos = id.join(snippet, how='inner')
        except ValueError:
            break     
        channel_videos_df.append(channel_videos)
        nextPageToken = json_data.get("nextPageToken")

    channel_videos_df = pd.concat(channel_videos_df)
    return channel_videos_df


def describe_channel(channel_id):
    '''
    Return channel information.

    channel_id = The channel id of the channel you would like to collect information about.
    '''
    channel_url = 'https://www.googleapis.com/youtube/v3/channels'
    request_url = channel_url+'?key='+api_key+'&textFormat=plainText&part=snippet,contentDetails,statistics&id='+channel_id +'&maxResults=50'
   
    # First request
    r = requests.get(request_url)  # request_url
    if r.status_code == 200:
        json_data = r.json()                                                                                                
        json_df = pd.DataFrame(json_data["items"])
        
        channel_info = pd.json_normalize(json_df['snippet'])  # need ['title', 'publishedAt'] for channel creation date
        channel_info = channel_info[['title', 'publishedAt']]
        channel_info.loc[0, 'authorChannelId'] = channel_id
        # channel_content_details = pd.json_normalize(json_df['contentDetails'])  # not useful 
        channel_statistics = pd.json_normalize(json_df['statistics'])
        channel_statistics.loc[0, 'authorChannelId'] = channel_id
        author_channel_info = pd.merge(left=channel_info, right=channel_statistics, left_on='authorChannelId', right_on='authorChannelId', how='inner')
        print(author_channel_info['authorChannelId'])
        return author_channel_info
    else:
        print(str(r.status_code))
        pass