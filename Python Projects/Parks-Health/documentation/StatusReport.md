# Status Report
By: Jack Damhorst, Ulyses Granados, Tarun Bathini
# Progress Updates
### Dataset Acquisition

- **CDC PLACES Dataset**:
  - Licensing requirements were reviewed. The data is available to us through the public domain.
  - API was accessed from the [CDC website](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data).
  - Successfully retrieved the dataset via API aligning with project requirements.
  - The script used to fetch the data programmatically is located in `data_acquisition.ipynb`.
  - Saved the raw data in `data/cdc.csv`.

- **ParkScore® Index Dataset**:
  - Licensing requirements were reviewed. Trust for Public Land has a copyright for its materials.
  - The copyright explains "you may download one copy of the information on this website for personal, non-commercial use. If you download, you may not modify the materials, use them for a commercial purpose or for public display, remove any copyright or trademark information, transfer the materials to another person, or allow unauthorized copying of the materials"
  - Since we will use this data for personal and educational purposes rather than commercial we will comply with the Trust for Public Land's user agreements.
  - 2022 Park Score Rankings were downloaded to match the timeframe of the CDC data.
  - Data was downloaded from Trust for Public Land's [Park Data Downloads](https://www.tpl.org/park-data-downloads).
  - The data originally links to a pdf for the ParkScore Index 2022 which was not formatted as a typical csv file.
  - The dataset was downloaded in an Excel format, exported as a csv, and processed to resolve formatting issues.
  - Relevant columns, such as `MedianParkSizeAcres`, `10MinWalkPercent`, and `EquityPoints`, were extracted.
  - Cleaned data was saved as `data/psi.csv`.
  - Preliminary cleaning and formatting tasks were performed within `data_acquisition.ipynb`.

- **Integrity Check**:
  - Both datasets were validated for consistency using SHA-256 checksums.
  - The hash validation scripts and corresponding checksum files can be found in:
    - CDC: `data_acquisition.ipynb`, `data/cdc.sha`
    - ParkScore®: `data_acquisition.ipynb`, `data/psi.sha`
### Dataset Cleaning

- **CDC Data**:
  - Cleaned and formatted for consistency.
  - Cleaned data was saved as `data/cdc.csv`.

- **ParkScore® Data**:
  - Addressed formatting inconsistencies in the Excel file:
    - Columns originally had ambiguous names such as `Data`, `Data.1`, `Data.2`, ... `Points\r\n/100`, `Points\r\n/100.2`, ... due to converting from a pdf to excel file to csv file.
    - Renamed columns to more descriptive names (e.g., `MedianParkSizeAcres`, `10MinWalkPercent`, `EquityPoints`) by evaluating the original pdf and mapping header names.
    - Extracted relevant fields for analysis.
  - Variable including the location name (City, State Abbreviation) was split into a `City` and `StateAbbr` column for schema and syntax consistency with the CDC dataset.
  - Cleaned and processed data was saved as `data/psi.csv`.
  - Cleaning scripts are stored in `data_acquistion.py`.

- **Documentation**:
  - Cleaning processes for both datasets were documented and initial findings were noted to include in the status report.

- **Challenges**:
  - The ParkScore Index data required extensive formatting due to mismatched column headers and non-standard naming conventions.

### Preliminary Integration

- **Integration Progress**:
  - Began integrating the cleaned CDC and ParkScore® datasets to prepare for analysis.
  - Key steps include:
    - Aligning geographic identifiers (e.g., matching cities and states across datasets).
    - Merging datasets to ensure consistency in metrics like `10MinWalkPercent` and `MedianParkSizeAcres`.
  - Read `data/psi.csv' and 'data/cdc.csv' from the data acquisition phase into pandas data frames.
  - Data frames could be merged using the `StateAbbr` column from the ParkScore Index data and the `stateabbr` column from the CDC data.
  - Data frames could also be merged using the `City` column from the ParkScore Index data and the `locationname` column from the CDC data.

 
### Exploratory Data Analysis

- **Progress**:
  - Began initial exploratory data analysis (EDA) on the cleaned datasets.
  - Key areas of focus include:
    - Identifying patterns in park access metrics such as `10MinWalkPercent` and `EquityPoints`.
    - Exploring health outcomes like obesity prevalence and physical activity levels in the CDC dataset.
    - Assessing data distributions and detecting any outliers or inconsistencies.

- **Artifacts**:
  - Integration script created: `data_integration.ipynb`.
  - Preliminary merged dataset will be saved as `data/integrated_data.csv` upon completion.

- **Challenges**:
  - Identifying common geographic keys between datasets required additional cleaning of location columns (e.g., splitting city and state names).
  - Differences in metric definitions between the two datasets (e.g., percentages versus raw counts) are being addressed during integration.
  - Integrated dataset may need some further cleaning to address messy data from the CDC data.
  - The ipynb files were used for interpretability and team communication, however, these may need to be changed to py files to ensure a smooth workflow.
  - The `data_acquisition.ipynb` file could be split up to include separate scrpits for data cleaning.
  - The acquisition ParkScore® Index Dataset was completed by downloading the dataset to our repository.
    - Our scripts should download the data at execution time to be consistent with project requirements.

- **Next Steps**:
  - Determine the method of integration between the CDC PLACES Dataset and the ParkScore® Index Dataset.
  - Continue refining EDA to better understand relationships between metrics and inform final statistical analysis.
  - Document key insights in the project report.

---

### Updated Timeline

| **Stage**                | **Status**         | **Deadline**          |
|-------------------------------|--------------------|-----------------------|
| Dataset acquisition           | Completed       | November 10, 2024    |
| Data cleaning and preparation | In progress    | November 18, 2024    |
| Exploratory data analysis     | In progress    | November 20, 2024    |
| Dataset integration           | Pending        | November 23, 2024    |
| Final data analysis           | Pending        | November 30, 2024    |
| Visualizations                | Pending        | December 3, 2024     |
| Final report writing          | Pending        | December 7, 2024     |

---

### Changes to the Plan

1. **Extended Cleaning Phase**:
   - Additional cleaning was required for the ParkScore® Index dataset due to formatting challenges in the downloaded Excel file.
   - This caused a slight delay in moving to the integration phase.
   - Scripts: `data_acquisition.ipynb`

2. **Added EDA Phase**:
   - Introduced an exploratory data analysis (EDA) step to better understand variables and refine the research questions.

---

### Next Steps 
  - Finalize the integration script in `data_integration.ipynb` and save the merged dataset as `data/integrated_data.csv`.
  - Organize scripts and data efficiently to help construct an automated end-to-end workflow in future steps.
  - Refine columns within the integrated dataset to include features that are relevant to our research.
  - Complete exploratory data analysis in and document findings for the report.
  - Code programmatic integration of the acquired datasets using Python/Pandas or SQL, ensuring smooth and logical merging of disparate data sources.
  - Collaborate in thorough data profiling, cleaning, and quality assessment to prepare the data for in-depth analysis.
  - Develop visualizations to represent the analysis findings with key metrics like `10MinWalkPercent`, `EquityPoints`, and health outcomes. Incorporate the analysis results and visualizations into the final report while ensuring the narrative is coherent and insightful.
  - Prepare for final statistical analysis by aligning methods with the project’s research questions.
  - Cite data and software used in the project accurately.
  - Verify the project's successful end-to-end workflow execution.
  - Create a reproducible package and metadata that describes the research.

