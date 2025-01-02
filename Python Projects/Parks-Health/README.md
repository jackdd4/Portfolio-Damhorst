# Parks and Cities

## Link to Archival Record
[DOI: 10.5072/zenodo.142299](https://sandbox.zenodo.org/records/142299)

## Contributors:
Jack Damhorst, Ulyses Granados, Tarun Bathini

## Summary

  In this project, our goal was to understand the relationship between public parks and public health.  We hoped to gain insights into the role parks play in enhancing public health in large cities across our nation. Furthermore, this research may inform urban planning and policy decisions aimed at promoting healthier, more resilient communities. Understanding the impact of green spaces could help identify opportunities for investment in public health through environmental design, ensuring cities prioritize green spaces to benefit all residents. 
  Our research question was "How does the availability of public parks in large cities correlate with obesity rates and physical activity levels among residents?" To explore this question, we collected two separate data sets and integrated them together for analysis. One of the datasets contained data relating to the parks in various U.S. locations and the other had data about public health in various U.S. locations. 
  To preprocess the data, we converted variable names to more interpretable terms and cleaned columns irrelevant to our research question. We also had to reshape the data frames so that they could be integrated together. After preprocessing, we were able to integrate the datasets by merging them using state abbreviations. This resulted in a dataset that had park information and health information for each state that had sufficient data. With this dataset, we could then conduct an analysis to try to answer our research question. 
  We developed a visualization that displays the relationship between the Trust for Public Land's park index ranking and the obesity percentage among adults in different states. This scatterplot was labeled using the state abbreviations so people could understand where each state stood when it came to park quality and obesity. The correlation could also be determined by examining the relationship displayed by the points. We then automated our whole workflow using Snakemake to make the project reproducible. This included defining rules for each programmatical step including data acquisition, data cleaning, data integration, and data analysis.

## Data Profile

1. Trust for Public Land - ParkScore® Index: The ParkScore® Index ranks cities in the U.S. based on park access, park investment, and park quality. The report includes data on how parks impact health indicators such as physical activity and obesity. This could be an excellent resource to measure park access and quality in relation to health outcomes. Trust for Public Land has a copyright for its materials. Under their Legal Disclosure and Terms of Use, they explain "you may download one copy of the information on this website for personal, non-commercial use. If you download, you may not modify the materials, use them for a commercial purpose or for public display, remove any copyright or trademark information, transfer the materials to another person, or allow unauthorized copying of the materials". Since we will be using this data for personal, educational purposes rather than commercial, we will be complying with the Trust for Public Land's user agreements and are permitted to use the data in our final project. Trust for Public Land - ParkScore® Report
2. CDC’s PLACES Project: The PLACES Project by the CDC provides local-level health data, including chronic disease indicators and health behaviors, which can be analyzed at the city or county level. This dataset covers outcomes like obesity, physical inactivity, and mental health, which you can relate to the availability of parks. Under Licensing and Attribution, the CDC explains that the data is public domain meaning it is not protected by intellectual property laws and we will be free to use it for our final project. CDC PLACES Project

The CDC data was collected via API from the [CDC website](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data) while the Trust for Public Land was downloaded from Trust for Public Land's [Park Data Downloads](https://www.tpl.org/park-data-downloads). The CDC data is accessible under the public domain while the Trust for Public Land data has some copyright restrictions which we follow accordingly.

The variables used in our analysis include the 'Rank' variable from the Trust for Public Land data and the `Obesity among Adults` data from CDC which we transformed into its own variable using the `Measure`, `Data_Value`, and `Data_Value_Unit` variables from the original dataset. The park score rankings from the Trust for Public Land is determined through 14 measures across five categories: acreage, investment, amenities, access, and equity. More information about the ParkScore ratings can be found [here](https://www.tpl.org/parkscore/rankings). The obesity percentages are estimates provided by the Centers for Disease Control and Prevention. The CDC data is from 2021-2022, so the Park Score ranking we used for the research was those from 2022 to maintain consistency.

## Findings 
We studied the relationship between public parks and obesity rates. Through our analysis of the two datasets, we developed a visualization that shows this relationship for different states. Our scatterplot, Obesity Rate vs Park Score Ranking By State, provides representation for 18 different states. The Obesity Rates and Park Scores were calculated by taking the mean from all the cities we had data for in each respective state. There are only 18 states included due to the sufficiency of data. The Rank measure comes from the Trust for Public Land and a lower score indicates higher park qualities for the state. Meanwhile, the Obesity Rate variable is represented as a percentage from the CDC. In the scatterplot, ideally, states would like to be in the top left quarter meaning there are quality parks and a low obesity rate. Of the states included, Colorado and Wisconsin are the most in this territory. On the other side, we see Louisiana and Oklahoma in the bottom right quarter of the plot showing these states have a high obesity rate and low park ranking. Some other interesting statistics found by our visualization are that Illinois had the highest ranking cities when it comes to park quality, Oklahoma had the lowest ranking cities when it comes to park quality, Louisiana had the highest obesity rate, and California had the lowest obesity rate. While it is interesting to observe where the states lie on the plot individually, our research intends to analyze the relationship between rank and obesity rate. Our graph indicates a weak correlation between these variables as there is not a clear linear relationship among the points. In fact, going across the x-axis, the rankings seem to go up as it nears the middle percentages at about an obesity rate of 36%, then drop down as the obesity rate increases further.

## Future Work
This research project was a good experience to apply the course concepts we have learned in IS 477. Our workflow and efforts towards reproducibility and transparency encompass important topics learned in this course. In the future, we hope to be able to apply the lessons learned from this project to work and education. As for our research question - How does the availability of public parks in large cities correlate with obesity rates and physical activity levels among residents - we will continue to search for data that may indicate a relationship between these variables as this is an important topic. We will also try to research how different variables in the CDC data set such as stroke, arthritis, and depression rates interact with other variables in the Park Score data set such as low-income park space scores or 10-minute walk scores. Understanding the relationship between public parks and public health can help improve the well-being of many.
## Reproducing

Steps to reproduce results:

1. Clone git repository
2. Download the 2022_ParkScoreRank.csv from input data in the [shared Box folder](https://uofi.app.box.com/folder/297795295066)
3. Create a folder named ```data``` at the root of the project repository and move the 2022_ParkScoreRank.csv there
4. Make sure necessary packages are installed from the requirements.txt file
5. Run the automated workflow by using ```snakemake all```

The visualization will be saved in the ```results``` folder

Data and software created as a part of this project is available through The MIT License

## References
* Centers for Disease Control and Prevention. (2024). PLACES: Local Data for Better Health, County Data 2022 release [Data set]. Retrieved from https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data
* Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2.
* J. D. Hunter, "Matplotlib: A 2D Graphics Environment", Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95, 2007.
* McKinney, W. (2010). Data structures for statistical computing in Python. In S. van der Walt & J. Millman (Eds.), Proceedings of the 9th Python in Science Conference (pp. 56–61). https://doi.org/10.25080/Majora-92bf1922-00a
* Microsoft. (2024). Visual Studio Code (Version 1.95). Retrieved from https://code.visualstudio.com
* Mölder, F., Jablonski, K.P., Letcher, B., Hall, M.B., Tomkins-Tinch, C.H., Sochat, V., Forster, J., Lee, S., Twardziok, S.O., Kanitz, A., Wilm, A., Holtgrewe, M., Rahmann, S., Nahnsen, S., Köster, J., 2021. Sustainable data analysis with Snakemake. F1000Res 10, 33.
* Python Software Foundation. (2024). Python programming language (Version 3.12). Retrieved from https://www.python.org
* Trust for Public Land. (2024). 2022 ParkScore® Rankings [Data Set]. Retrieved from https://www.tpl.org/park-data-downloads
* Waskom, M. L., (2021). seaborn: statistical data visualization. Journal of Open Source Software, 6(60), 3021, https://doi.org/10.21105/joss.03021.