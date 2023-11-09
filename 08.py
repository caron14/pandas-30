import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    """
    Note:
        - `^` indicates the start of a string or line
        - `[a-z]*` indicates a character range, matching any character from a to z zero or more times.
        - `[a-z]+` indicates a character range, matching any character from a to z one or more times.
        - `.` indicates the matche exactly one of any character
        - `$` indicates the end of a string or line
    """
    return users[users["mail"].str.match(r"^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\.com$")]


"""SQL
SELECT user_id, name, mail
FROM Users
-- Note that we also escaped the `@` character, as it has a special meaning in some regex flavors
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*\\@leetcode\\.com$';
"""
