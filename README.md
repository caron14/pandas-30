# Pandas Practice Repository

A collection of 8 hands-on exercises that demonstrate how to convert SQL queries into pandas DataFrame operations. Each challenge focuses on essential data manipulation patterns commonly used in data analysis.

## What You'll Learn

- **Data Filtering**: Boolean indexing with multiple conditions
- **String Operations**: Length validation, case formatting, regex pattern matching
- **Data Relationships**: Anti-joins and set operations
- **Deduplication**: Removing duplicates with sorting
- **Conditional Logic**: Applying business rules with lambda functions
- **Column Manipulation**: Selecting, renaming, and transforming data

## Structure

Each numbered file (`01.py` through `08.py`) contains:
- A function solving a specific data problem using pandas
- The equivalent SQL query as a reference comment
- Multiple solution approaches where applicable

## Quick Start

```python
import pandas as pd
from 01 import big_countries

# Create sample data
world_data = pd.DataFrame({
    'name': ['China', 'USA', 'India'],
    'population': [1400000000, 330000000, 1380000000],
    'area': [9596961, 9833517, 3287263]
})

# Test the function
result = big_countries(world_data)
print(result)
```

## Exercise Topics

1. **Country Analysis** - Filter by area and population thresholds
2. **Product Filtering** - Multiple boolean conditions
3. **Customer Analysis** - Find customers without orders (anti-join)
4. **Article Views** - Self-referencing filters with deduplication
5. **Tweet Validation** - String length filtering
6. **Employee Bonuses** - Conditional calculations
7. **Name Formatting** - String case manipulation
8. **Email Validation** - Regex pattern matching

Perfect for beginners learning pandas or those transitioning from SQL to Python data analysis.