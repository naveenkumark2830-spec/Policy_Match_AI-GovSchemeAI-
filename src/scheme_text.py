import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(BASE_DIR, "data", "cleaned_schemes.csv")
output_path = os.path.join(BASE_DIR, "data", "schemes_with_text.csv")

df = pd.read_csv(input_path)

df["scheme_text"] = (
    df["scheme_name"].astype(str)
    + " "
    + df["details"].astype(str)
    + " "
    + df["benefits"].astype(str)
    + " "
    + df["eligibility"].astype(str)
    + " "
    + df["schemeCategory"].astype(str)
    + " "
    + df["tags"].astype(str)
)

df.to_csv(output_path, index=False)

print(df[["scheme_name", "scheme_text"]].head())