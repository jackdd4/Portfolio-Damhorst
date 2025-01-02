import pandas as pd
import hashlib

# API URL for the CDC dataset
url = "https://data.cdc.gov/resource/swc5-untb.csv"
cdc_df = pd.read_csv(url)

# Read the downloaded PSI data into a Pandas DataFrame
psi_df = pd.read_csv('data/2022_ParkScoreRank.csv', header=7, encoding='utf-8')

# Check integrity
cdc_df.to_csv('data/cdc.csv', index=False)

with open("data/cdc.csv", "rb") as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

with open("data/cdc.sha", "w") as f:
    f.write(sha256hash)

psi_df.to_csv('data/psi.csv', index=False)

with open("data/psi.csv", "rb") as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

with open("data/psi.sha", "w") as f:
    f.write(sha256hash)
    
