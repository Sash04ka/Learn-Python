"""
expenses.py:
1. Reads expenses.csv
2. Builds summaries
3. Writes them back to disk

pivot_daily.csv        : rows = dates, columns = categories, numbers = daily sums
totals_by_category.csv : one row per category with the grand-total amount

"""
# packages
import pandas as pd

# load raw CSV
df = pd.read_csv('expenses.csv', parse_dates=['dt'])

# date x category pivot
pivot = (
    df.pivot_table(
        index='dt',
        columns='category',
        values='amount',
        aggfunc='sum',
        fill_value=0
    )
    .round(2)
)
# totals per category of expense
totals = (
    df.groupby('category', as_index=False)["amount"]
    .sum()
)
# save the results
pivot.to_csv("pivot_daily.csv")
totals.to_csv("totals_by_category.csv", index=False)

print("Done, pivot and totals are ready!")
