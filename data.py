import pandas as pd

# Read CSV files
file_paths = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
dfs = [pd.read_csv(path) for path in file_paths]

# Data filtering, transformation and merging
filtered_dfs = []
for df in dfs:
    # Keep `Pink Morsels`
    filtered_df = df[df['product'] == 'pink morsel']
    # Remove the $ in the price
    filtered_df['price'] = filtered_df['price'].replace('[\$,]', '', regex=True).astype(float)
    # calculate `sales`
    filtered_df['sales'] = filtered_df['quantity'] * filtered_df['price']
    filtered_df['sales'] = filtered_df['sales'].apply(lambda x: f"${x:.2f}")
    # Keep required fields
    filtered_df = filtered_df[['sales', 'date', 'region']]
    filtered_dfs.append(filtered_df)

# Merge all DataFrame
final_df = pd.concat(filtered_dfs)

# Output to CSV
final_df.to_csv('output.csv', index=False)