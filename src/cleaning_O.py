import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(BASE_DIR, "data", "updated_data.csv")
output_path = os.path.join(BASE_DIR, "data", "cleaned_schemes.csv")

# Load dataset
df = pd.read_csv(input_path)

print("Before Cleaning")
print(df.shape)
print(df.columns)

# Remove unnamed columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("")

print("\nAfter Cleaning")
print(df.shape)

# Save cleaned dataset
df.to_csv(output_path, index=False)

print("Dataset Cleaned Successfully")