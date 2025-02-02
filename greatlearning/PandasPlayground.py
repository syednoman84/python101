import pandas as pd

# Read a CSV file into a DataFrame
data_customer = pd.read_csv("customers.csv")

print(data_customer.groupby(['sales'])['customer'].mean())
# print(data_customer.loc[[1,2], ['customer', 'sales']])
# print(data_customer.sort_values(by='sales',ascending=False))
# print(data_customer.sort_values(by='sales',ascending=False))
# print(data_customer['category'].unique())
# print(data_customer['category'].value_counts())
# print(data_customer['customer'].value_counts())
# print(data_customer(['category'])['customer'].value_counts())






# Explore the DataFrame
# print(df.head())  # Display the first few rows
# print(df.info())  # Summary of the DataFrame

# Perform some operations
# df['new_column'] = df['existing_column'] * 2  # Add a new column
# df_filtered = df[df['column_name'] > 10]  # Filter rows
#
# # Write DataFrame to a new CSV file
# df.to_csv("output.csv", index=False)