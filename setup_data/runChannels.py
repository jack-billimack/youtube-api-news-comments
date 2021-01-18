'''
WHEN RESEARCHING TOP NEWS CHANNELS, I FOUND THESE URL PARAMETERS ON YOUTUBE

# FOX
channel_id = 'UCXIJgqnII2ZOINSWNOGFThA'
# user_id = 'FoxNewsChannel'

# CNN
channel_id = 'UCupvZG-5ko_eiXAupbDfxWw' # is channel(channelListResponse), runs make_channel_videos_dataframe
# user_id = 'CNN'

# MSNBC
channel_id = 'UCaXkIU1QidjPwiAYu6GcHjg' 
other_id = 'msnbc'
# user_id = 'msnbcleanforward'  
'''
try:
    import pandas as pd
    video_master = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\channel_videos\\all_videos.csv')
except:
    from getYoutubeChannelData import make_channel_videos_dataframe
    import pandas as pd

    # TODO: FIND LIST OF YOUTUBE VIDEOS FROM DIFFERENT NETWORKS, COVERING THE SAME TOPICS
    test_videos = {
        'network_channels': {'fox': 'UCXIJgqnII2ZOINSWNOGFThA', 'cnn': 'UCupvZG-5ko_eiXAupbDfxWw', 'msnbc': 'UCaXkIU1QidjPwiAYu6GcHjg'}
    }
    df_channels = pd.DataFrame.from_dict(test_videos, orient='index') 

    fox_videos = make_channel_videos_dataframe(df_channels['fox'][0])
    cnn_videos = make_channel_videos_dataframe(df_channels['cnn'][0])
    msnbc_videos = make_channel_videos_dataframe(df_channels['msnbc'][0])
    # Makes sense to save these channel DataFrames _.to_csv('/path/to.csv')

    video_master = pd.concat([fox_videos, cnn_videos, msnbc_videos])

video_master_final = video_master[['Unnamed: 0', 'kind', 'videoId', 'publishedAt', 'channelId', 'title',
       'description', 'channelTitle', 'liveBroadcastContent', 'publishTime']].drop(columns=['Unnamed: 0'])