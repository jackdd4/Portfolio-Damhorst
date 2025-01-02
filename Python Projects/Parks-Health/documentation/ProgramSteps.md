## Data Acquisition
* CDC data was acquired using this API URL: https://data.cdc.gov/resource/swc5-untb.csv
* 2022 Park Score Ranking data was downloaded and placed into data folder at root of repository from this site: https://www.tpl.org/park-data-downloads
* Check sums were implemented using the hashlib library from Python
## Data Cleaning
* Transformed CDC dataset to have variable names for distinct measures with their data values
* Grouped the CDC dataset by state abbreviations and aggregated measures by mean
* Renamed PSI columns to more interpretable terms
* Extracted state abbreviations in the City column of the PSI data set
* Grouped the PSI dataset by state abbreviations and aggregated numeric variables by mean
## Data Integration
* Merged CDC and PSI dataframes using state abbreviation
## Data Analysis
* Utilized matplotlib and seaborn to generate a scatterplot visualization of relationship between ```with Obesity among adults``` and ```Rank``` variables while labelling by state
## Automated Workflow
* Created a Snakefile with four rules (collect_data, clean_data, integrate_data, analyze_data) for each of the previous steps as well as a rule to run all
