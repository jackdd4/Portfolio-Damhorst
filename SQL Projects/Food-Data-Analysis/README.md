# Fixing a Cluttered Food Sales Dashboard

## 📌 What is this project?
This repository contains a SQL backend and the initial design stage of a dashboard tracking food industry sales data. 

Right now, the current version of the dashboard (`FoodDataDashboard.png`) is functional, but it's tough to read and doesn't tell a clean story. I am using this project to document my process as I rewrite the underlying SQL queries and completely clean up the frontend layout to make it user-friendly for business stakeholders.

## 🛠️ What's wrong with the current dashboard?
Looking closely at the staging version (`FoodDataDashboard.png`), a few major things need to be fixed to make it readable at a glance:

* **Text and Layout Formatting:** The top KPI cards (like Total Revenue) and chart titles feel crowded at the margins. The layout needs more breathing room and intentional padding to separate the high-level metrics from the underlying visualizations.
* **Bad Chart Selection:** The top-right visual uses a statistical Box Plot to show sales by city. While box plots are great for advanced stats, they are confusing for standard reporting. A stakeholder shouldn't have to guess at quartiles just to see which city sold the most.
* **Visual Overload:** The center stacked bar chart breaks categories down by individual product names. Because there are so many products, it creates a dozen tiny color slices that are impossible to compare visually.
* **Zero Breathing Room:** The bottom-right corner is incredibly crowded. The treemap, pie chart, and legends are all squished together, causing text to clip and burying the regional breakdown.

## 🚀 The Fixes I'm Working On
I am actively overhauling the reporting structure to focus on clarity and clean design:

* **Clean KPI Cards:** Moving `Total Revenue` and `Total Units Sold` into their own dedicated, well-padded boxes at the top left so they are the first thing you see.
* **Ditching the Box Plot:** Swapping the city box plot out for a simple, sorted **Horizontal Bar Chart** so city performance reads like a clear leaderboard.
* **Streamlining the Products:** Grouping the long list of specific products into a clean "Top 10" view so the charts aren't a rainbow of tiny slices.
* **Adding Whitespace:** Giving the bottom-right charts room to breathe, separating the visuals, and adding explicit percentage labels to the regional data.
* **SQL Cleanup:** Tweaking the aggregation layers in `fooddata.sql` so the dashboard loads instantly without lagging.

## 🧰 Tools Used
* **SQL:** Data cleaning and extraction (code is in `fooddata.sql`).
* **BI / Visualization:** [Specify your tool here, e.g., Power BI / Tableau / Excel] for the dashboard layout.

## 📂 Files in this Folder
* `fooddata.sql` - The queries used to pull and aggregate the data.
* `FoodDataDashboard.png` - The original, messy dashboard staging view I am currently redesigning.
