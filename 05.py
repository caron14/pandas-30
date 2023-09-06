import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets["invalid_flag"] = tweets["content"].apply(
        lambda x: True if len(x) > 15 else False
    )
    return tweets[tweets["invalid_flag"] == True][["tweet_id"]]


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    print(tweets["content"].str.len())
    return tweets[tweets["content"].str.len() > 15][["tweet_id"]]


"""SQL
SELECT 
    tweet_id
FROM 
    tweets
WHERE 
    CHAR_LENGTH(content)> 15
"""
