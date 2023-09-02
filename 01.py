import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world["area"] >= 3000000) | (world["population"] >= 25000000)][
        ["name", "population", "area"]
    ]


"""SQL
SELECT 
    * 
FROM 
    world 
WHERE 
    area >= 3000000 
    OR population >= 25000000
"""
