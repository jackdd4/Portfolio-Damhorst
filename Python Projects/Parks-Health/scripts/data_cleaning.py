import pandas as pd
import numpy as np

# Clean CDC data
cdc_df = pd.read_csv('data/cdc.csv')

# Define measures to be analyzed
measures = [
    'Stroke among adults',
    'Arthritis among adults',
    'Obesity among adults',
    'Depression among adults'
]

cdc_df = cdc_df[cdc_df['measure'].isin(measures)].reset_index()

for measure in measures:
    cdc_df[measure] = None

for measure in measures:
    cdc_df.loc[
        cdc_df['measure'] == measure, measure
    ] = cdc_df.loc[
    cdc_df['measure'] == measure, 'data_value'
    ]

# Include relevant columns and grouping by state
cdc_columns = ['stateabbr'] + measures
cdc_df = cdc_df[cdc_columns].groupby('stateabbr').agg('mean').reset_index()

cdc_df.to_csv('data/cleaned_cdc.csv', index=False)

# Clean PSI data
psi_df = pd.read_csv('data/psi.csv')

# Rename columns
psi_df = psi_df.rename(columns={
    'City' : 'CityState',
    'Data (Acres)' : 'MedianParkSizeAcres',
    'Points\r\n/100' : 'MedianParkSizePoints',
    'Data' : 'ParklandPercent',
    'Points\r\n/100.1' : 'ParklandPoints',
    'Acreage Points/100' : 'AceragePoints',
    'Data.1' : '10MinWalkPercent',
    'Points\r\n/100.2' : '10MinWalkPoints',
    'Data.2' : 'POC10MinWalkPercent',
    'Points\r\n/100.3' : 'POC10MinWalkPoints',
    'Data.3' : 'LowIncome10MinWalkPercent',
    'Points\r\n/100.4' : 'LowIncome10MinWalkPoints',
    'Data.4' : 'POCParkSpacePercent',
    'Points /100' : 'POCParkSpacePoints',
    'Data.5' : 'LowIncomeParkSpacePercent',
    'Points /100.1' : 'LowIncomeParkSpacePoints',
    'Equity Points/100' : 'EquityPoints',
    'Data.6' : 'SpendingPerResident',
    'Points\r\n/100.5' : 'SpendingPoints'
})

# Extract state abbreviation 
psi_df['stateabbr'] = psi_df['CityState'].apply(
    lambda x: str(x).split(', ')[-1]
)

psi_columns = [
    'Rank',
    'stateabbr',
    'MedianParkSizeAcres',
    'MedianParkSizePoints',
    'ParklandPercent',
    'ParklandPoints',
    'AceragePoints',
    '10MinWalkPercent',
    '10MinWalkPoints',
    'POC10MinWalkPercent',
    'POC10MinWalkPoints',
    'LowIncome10MinWalkPercent',
    'LowIncome10MinWalkPoints',
    'POCParkSpacePercent',
    'POCParkSpacePoints',
    'LowIncomeParkSpacePercent',
    'EquityPoints',
    'SpendingPerResident',
    'SpendingPoints'
]

psi_df = psi_df[psi_columns]

# Specify columns with numeric data types 
psi_df["Rank"] = psi_df["Rank"].replace("n.a.", np.nan)
psi_df["Rank"] = pd.to_numeric(psi_df["Rank"])

psi_num_columns = list(
    psi_df.select_dtypes(include=["number"]).columns
) + ['stateabbr']

# Group by state
psi_df = psi_df[psi_num_columns].groupby('stateabbr').agg('mean').reset_index().dropna()

psi_df.to_csv('data/cleaned_psi.csv', index=False)

