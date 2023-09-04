import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers["id"].isin(orders["customerId"])]
    df.rename(columns={"name": "Customers"}, inplace=True)
    return df[["Customers"]]


"""SQL
select *
from customers
where customers.id not in
(
    select customerid from orders
);
"""
