# Metadata for Trust for Public Land ParkScore® Index Data

## Description
This dataset, sourced from the Trust for Public Land ParkScore® Index, provides detailed information on public parks in cities across the United States. It includes variables such as park acreage, investment, accessibility, amenities, and equity. These data points are crucial for understanding the relationship between park access and community health indicators.

## Columns Description
- **stateabbr:** Abbreviation of the U.S. state.  
- **Rank:** The overall rank of the city/state based on park metrics.  
- **MedianParkSizePoints:** Points assigned based on the median size of parks in the city/state.  
- **ParklandPoints:** Points assigned based on the percentage of land area dedicated to parks.  
- **AcreagePoints:** Points assigned based on the total acreage of parkland.  
- **10MinWalkPoints:** Points for the percentage of residents within a 10-minute walk to a park.  
- **POC10MinWalkPoints:** Points for people of color within a 10-minute walk to a park.  
- **LowIncome10MinWalkPoints:** Points for low-income individuals within a 10-minute walk to a park.  
- **POCParkSpacePoints:** Points assigned for the equity of park space allocation for people of color.  
- **EquityPoints:** Overall points assigned for equity in park access.  
- **SpendingPoints:** Points for park-related spending per resident.

## Source
Trust for Public Land ParkScore® Index  
[Website Link](https://www.tpl.org/parkscore)

## Data Collection Date
2022

## Licensing Information
The dataset is under a restrictive license from the Trust for Public Land, intended for personal and educational use. Redistribution or modification of the dataset is not permitted.

## Data Transformation Details
The following transformations were performed on the original dataset:  
- Variable names were renamed for readability and clarity.  
- Irrelevant columns were removed to focus on variables relevant to the research question.  
- Any null or missing values were handled through imputation or deletion where appropriate.

## Known Issues
- Data is limited to 2022 and does not account for year-over-year trends.  
- Some cities may lack complete data, leading to potential gaps in analysis.

## Usage
This dataset is being used in conjunction with health data from the CDC to examine the relationship between park access and health outcomes such as obesity and mental health. It is stored as `cleaned_psi.csv` in the project repository.
