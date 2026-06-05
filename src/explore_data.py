import pandas as pd

# Load the dataset
df = pd.read_csv('data/emails.csv')

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Total emails:     {df.shape[0]}")
print(f"Total features:   {df.shape[1] - 2}")
print(f"\nSafe emails:      {(df['Prediction'] == 0).sum()}")
print(f"Phishing emails:  {(df['Prediction'] == 1).sum()}")
print(f"\nFirst 5 columns:  {df.columns[:5].tolist()}")
print(f"Last column:      {df.columns[-1]}")
print("=" * 50)