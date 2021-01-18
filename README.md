# Gather Youtube channel videos and their comment metadata
> Use the Youtube API in Python to mine textual data

## The Youtube API
[Youtube Search Data API](https://developers.google.com/youtube/v3/docs/search)
[Youtube Channels Data API](https://developers.google.com/youtube/v3/docs/channels/list)
[Youtube CommentThreads Data API](https://developers.google.com/youtube/v3/docs/commentThreads/list)

## The Script Data
Out of interest from an Economist publishing posting, I thought it could be interesting to analyze Youtube comment statistics across the top 3 News outlets in the USA.
https://www.statista.com/statistics/373814/cable-news-network-viewership-usa/
{
    'date': 2020-06
    'network':
    
        "FOX NEWS": {
            viewership: 
                {'primetime': 3,978,000, 'ages_25-54': 792,000}
        }, 
        "CNN": {
            viewership: 
                {'primetime': 2,510,000, 'ages_25-54': 880,000}
        },
        "MSNBC": {
            viewership: 
                {'primetime': 2,266,000, 'ages_25-54': 401,000}
        }
}

I was able to access Youtube's API, but time ran out before I could dig into deeper statistical analysis. This repo's current state is a workflow for gathering Youtube videos and associated comments for 3 news outlets.

## The Application Flow
getYoutubeChannelData uses [Youtube Search Data API](https://developers.google.com/youtube/v3/docs/search) in make_channel_videos_dataframe() to return channel_video_df
getYoutubeChannelData uses [Youtube Channels Data API](https://developers.google.com/youtube/v3/docs/channels/list) in describe_channel() to return author_channel_info (descriptive only... not necessary)
|
|__> runChannels calls make_channel_videos_dataframe() for each channel we are interested in. In this case, Fox News, CNN, and MSNBC.
  _> runChannels then concatenate these dataframes into one large dataframe (video_master_final).
        |__> video_master[['kind', 'videoId', 'publishedAt', 'channelId', 'title', 'description', 'channelTitle', 'liveBroadcastContent', 'publishTime']]

Once you have gathered the list of Youtube Channels and videos you want to gather comments for, we use the Youtube CommentThreads Data API.
getYoutubeVideoComments uses [Youtube CommentThreads Data API](https://developers.google.com/youtube/v3/docs/commentThreads/list) in make_comment_dataframe() to return comment_df
|
|__> runVideos imports the video_master_final dataframe with all videos to gather comments for.  runVideos calls make_comment_df() from within gather_video_comments(). Youtube's CommentThreads Data API has a free quota of 10,000 queries per day which means we use gather_video_comments to iterate on the list of videos remaining.
    |_>Once we gather all the comments we want, we concatenate and format the final dataframe to comment_master_final

## Analysis #TODO:(s)
Questions to answer:
[1]-how long has the commenting account been active for
[2]-how many videos has the account commented on
[3]-how many likes does the account recieve
[4]-how many videos have the accounts commented on, by news channel grouping
[5]-what percent of the commenting channel's comments go to one of the three news channels
[6]-how many words does the account average
[7]-how many grammar errors does the channel's comments have
[8]-what is the vocabulary level of the channel's comments
[9]-do channels cover the same topics
[10]-inappropriate names by grouping, single word names by grouping(pseudonym)
[11]-how many commenting users have commented on one of the other news sites listed
[12]-how do the same topics garner sentiment across Youtube news channels
