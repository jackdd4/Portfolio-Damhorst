### Metadata for cleaned_cdc.csv

#### Dataset Overview
- **Name**: CDC Cleaned Health Data (cleaned_cdc.csv)
- **Source**: Centers for Disease Control and Prevention (CDC)
- **Description**: This dataset provides health indicators across U.S. states, including stroke prevalence, arthritis, obesity, and depression rates among adults.
- **Purpose**: To analyze correlations between public health metrics and environmental factors like park access.
- **File Format**: CSV
- **Date Created**: December 2024

#### Variables
1. **stateabbr**
   - **Description**: State abbreviation.
   - **Type**: Categorical
   - **Example**: `AK` (Alaska), `AL` (Alabama)

2. **Stroke among adults**
   - **Description**: Prevalence of strokes among adults in the state (percentage).
   - **Type**: Numerical (Float)
   - **Example**: `4.47`

3. **Arthritis among adults**
   - **Description**: Percentage of adults with arthritis in the state.
   - **Type**: Numerical (Float)
   - **Example**: `23.53`

4. **Obesity among adults**
   - **Description**: Prevalence of obesity among adults in the state (percentage).
   - **Type**: Numerical (Float)
   - **Example**: `32.4`

5. **Depression among adults**
   - **Description**: Percentage of adults reporting depression in the state.
   - **Type**: Numerical (Float)
   - **Example**: `19.27`

#### Data Quality and Cleaning
- **Source Reliability**: Public domain data provided by the CDC.
- **Data Cleaning Steps**:
  - Converted original variable names to more readable formats.
  - Filtered out irrelevant columns from the original CDC dataset.
  - Removed missing or inconsistent values.
  - Normalized data for consistent formatting.

#### Licensing and Use
- **License**: Public domain (as specified by CDC licensing agreements).
- **Usage**: Data is free for educational and research purposes with proper attribution.

#### Link to Raw Data Source
- **URL**: [CDC Data Portal](https://data.cdc.gov/)

#### Integration
- **Merged With**: Trust for Public Land ParkScore® dataset (cleaned_psi.csv) using state abbreviations.
- **Purpose of Integration**: To analyze the relationship between health indicators and park access/quality.

#### Notes for Reproducibility
1. Ensure the file is saved in the `data/` directory at the root of the project repository.
2. Check for consistent formatting (e.g., numeric values have no trailing zeros).
3. Refer to the documentation on integration processes to align datasets.
