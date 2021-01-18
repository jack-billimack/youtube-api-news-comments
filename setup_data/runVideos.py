from setup_data.runChannels import video_master_final
from setup_data.getYoutubeVideoComments import make_comment_dataframe
import pandas as pd

comment_master = []

def gather_video_comments():
    '''
    This video gathers video comments from the list of videos identified from 
    setup_data.runChannels's DataFrame video_master. 
    The Youtube Data API has a 10,000 query per day limit and allows 1,800,000
    queries per minute, according to GCP.
    
    Sets' last videos:
    [1] - WmYGT3iJEZE - i:109 -- for video_id in video_master['videoId']:
    [2] - 1111
    '''
    for video_id in video_master_final['videoId'][1111:]:
        try:
            comment_df = make_comment_dataframe(video_id)
            comment_master.append(comment_df)
        except Exception as e:
            print(e)

gather_video_comments()

comment_master.to_csv('\\PATH\\TO\\YoutubeCommentors\\data\\video_comments\\all_comments_xx.csv')



# combine comment dfs
com_1 = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\video_comments\\all_comments_10202020.csv')
com_2 = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\video_comments\\all_comments_10212020.csv')
com_3 = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\video_comments\\all_comments_10232020.csv')
com_4 = pd.read_csv('\\PATH\\TO\\YoutubeCommentors\\data\\video_comments\\all_comments_10292020.csv')
for file in [com_1, com_2, com_3, com_4]:
    print(len(file))
comment_master_final = pd.concat([com_1, com_2, com_3, com_4], ignore_index=True)

comment_master_final = comment_master_final[['videoId', 'canReply', 'totalReplyCount', 'isPublic',
       'topLevelComment.kind', 'topLevelComment.etag', 'topLevelComment.id',
       'topLevelComment.snippet.textDisplay',
       'topLevelComment.snippet.textOriginal',
       'topLevelComment.snippet.authorDisplayName',
       'topLevelComment.snippet.authorChannelId.value',
       'topLevelComment.snippet.canRate',
       'topLevelComment.snippet.viewerRating',
       'topLevelComment.snippet.likeCount',
       'topLevelComment.snippet.publishedAt',
       'topLevelComment.snippet.updatedAt',
       'topLevelComment.snippet.moderationStatus'
       ]]
comment_master_final.columns = ['videoId', 'canReply', 'totalReplyCount', 'isPublic',
       'topLevelComment.kind', 'etag', 'comment_id',
       'textDisplay',
       'textOriginal',
       'authorDisplayName',
       'authorChannelId',
       'canRate',
       'viewerRating',
       'likeCount',
       'publishedAt',
       'updatedAt',
       'moderationStatus']
# Drop duplicates from running gather_video_comments multiple times over multiple days for API Quota limits
comment_master_final.to_csv('\\PATH\\TO\\YoutubeCommentors\\data\\video_comments\\all_comments_prod.csv')