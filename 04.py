import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views["author_id"] == views["viewer_id"]]
    df = df[["author_id"]].rename(columns={"author_id": "id"})
    df = df[~df.duplicated(subset=["id"], keep="first")].sort_values(
        by=["id"], ascending=True
    )
    return df


"""SQL
SELECT 
    DISTINCT author_id AS id 
FROM 
    Views 
WHERE 
    author_id = viewer_id 
ORDER BY 
    id 
"""
