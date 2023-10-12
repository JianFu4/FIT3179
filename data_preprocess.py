import pandas as pd

# Load your main dataset
df_main = pd.read_csv("https://raw.githubusercontent.com/JianFu4/FIT3179/main/global-data-on-sustainable-energy%20(1).csv")

# Load your country-region dataset (assuming it's named 'regions.csv')
df_regions = pd.read_csv("regions.csv")

# Merge the datasets on the respective columns
merged_df = pd.merge(df_main, df_regions, left_on="Entity", right_on="name", how="left")

# Drop duplicate or unnecessary columns if needed (like 'name' from the second dataset)
merged_df.drop('name', axis=1, inplace=True)

# Save the merged DataFrame back to CSV if needed
merged_df.to_csv("merged_dataset.csv", index=False)
