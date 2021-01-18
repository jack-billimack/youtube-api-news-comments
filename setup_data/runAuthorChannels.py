import pandas as pd

# id_fox = 'UCXIJgqnII2ZOINSWNOGFThA'
# id_cnn = 'UCupvZG-5ko_eiXAupbDfxWw' 
# id_msnbc = 'UCaXkIU1QidjPwiAYu6GcHjg' 

# news_comments = df['authorChannelId'].isin([id_fox, id_cnn, id_msnbc])
# df_cleaner = df[~news_comments]  # the news channels do not comment on their videos, all good

try: 
    authorChannels = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\commentor_ids\\authorChannels.csv')
    authorChannels = list(authorChannels['authorChannelId'].unique())
except:
    from join_videos_comments import video_comments
    video_comments['authorChannelId'].value_counts()  # Quick look
    authorChannels = list(video_comments['authorChannelId'].unique())

from getYoutubeChannelData import describe_channel

# 1: [:10000]
# 2: [49065:] authorChannels.index("UCcRAbNLtx5aY4OkhHfR6v9g")
# 3: [644106:] authorChannels.index("UCsQzZFLDTcjGn_egXtpHBiQ")

################################
# DOUBLE CHECK THE LIST OF authorChannelIds not in the output of commentor_channel_info, find them, run them
c_channels1 = pd.read_csv('D:\Users\jackb_HDD\Development\Ideas\YoutubeCommentors\data\commentor_channel_info\commentor_channel_info.csv')
c_channels2 = pd.read_csv('D:\Users\jackb_HDD\Development\Ideas\YoutubeCommentors\data\commentor_channel_info\commentor_channel_info2.csv')
c_channels3 = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\commentor_channel_info\\commentor_channel_info3.csv')

authorChannels_complete = []
authorChannels_complete.extend(list(c_channels3['authorChannelId']))
authorChannels_complete.extend(list(c_channels2['authorChannelId']))
authorChannels_complete.extend(list(c_channels1['authorChannelId']))
authorChannels_complete = pd.DataFrame({'authorChannel_complete':authorChannels_complete})

import numpy as np

loop_list = np.setdiff1d(authorChannels,authorChannels_complete)
################################

author_channel_master = []

for account_id in loop_list: #authorChannels[644106:]
    try:
        author_channel_info = describe_channel(account_id)
        author_channel_master.append(author_channel_info)
    except Exception as e:
        print(e)

# TODO:
commentor_channel_info3 = pd.concat(author_channel_master)
# send video_comments to D:\Users\jackb_HDD\Development\Ideas\YoutubeCommentors\data\commentor_channel_info\commentor_channel_info123.csv


