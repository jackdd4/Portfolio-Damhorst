import pandas as pd

# Load cleaned PSI and CDC datasets
psi_df = pd.read_csv('data/cleaned_psi.csv')
cdc_df = pd.read_csv('data/cleaned_cdc.csv')

# Merge datasets using state abbreviations
df = psi_df.merge(cdc_df, on='stateabbr') #datasets are merged using state abbreviations

# Save the integrated dataset to a CSV file
df.to_csv('data/integrated.csv', index=False)
