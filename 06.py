import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees.apply(
        lambda row: row["salary"]
        if (row["employee_id"] % 2 == 1) & (row["name"][0] != "M")
        else 0,
        axis=1,
    )
    employees.sort_values(by=["employee_id"], ascending=True, inplace=True)
    return employees[["employee_id", "bonus"]]


"""SQL
SELECT 
    employee_id,
    IF(employee_id % 2 = 1 AND name NOT REGEXP '^M', salary, 0) AS bonus 
FROM 
    employees 
ORDER BY 
    employee_id
"""
