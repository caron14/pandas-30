import pandas as pd

# Solution 1
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].apply(lambda x: f"{x[0].upper()}{x[1:].lower()}")
    return users.sort_values(by=["user_id"])


# Solution 2
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str[0].str.upper() + users["name"].str[1:].str.lower()
    return users.sort_values(by=["user_id"])


"""SQL
SELECT user_id, CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;
"""
