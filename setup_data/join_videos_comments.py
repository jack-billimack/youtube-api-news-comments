import pandas as pd

# TODO: merge the data into a master dataframe
try:
    video_comments = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\news_videos_w_comments\\video_comments.csv')
except:
    try:
        video_master_final = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\channel_videos\\video_metadata.csv')
    except:
        from setup_data.runChannels import video_master_final
    try: 
        comment_master_final = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\video_comments\\all_comments_prod.csv')
        # CNN comments likely not picked up above ^ will need to rerun runVideos with list of CNN videos
    except:
        from setup_data.runVideos import comment_master_final

    video_comments = pd.merge(left=video_master_final, right=comment_master_final, left_on=['videoId'], right_on=['videoId'], how='right')

video_comments = video_comments.loc[:, ~video_comments.columns.str.contains('^Unnamed')]
video_comments.columns = ['kind', 'videoId', 'publishedAt_video', 'channelId', 'title', 'description',
       'channelTitle', 'liveBroadcastContent', 'publishTime', 'canReply',
       'totalReplyCount', 'isPublic', 'topLevelComment_kind', 'etag',
       'comment_id', 'textDisplay', 'textOriginal', 'authorDisplayName',
       'authorChannelId', 'canRate', 'viewerRating', 'likeCount',
       'publishedAt_comment', 'updatedAt_comment', 'moderationStatus']

# df.to_csv('\\PATH\\TO\\YoutubeCommentors\\data\\news_videos_w_comments\\video_comments2.csv')