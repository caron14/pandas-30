import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[
        (products["low_fats"] == "Y") & (products["recyclable"] == "Y")
    ].loc[:, ["product_id"]]


"""SQL
SELECT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND recyclable = 'Y'
"""
