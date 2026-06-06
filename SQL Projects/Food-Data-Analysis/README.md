# Food Data Analysis & Dashboard Redesign

## 📌 Project Overview
This data analytics project focuses on extracting, cleaning, and aggregating food industry sales datasets using SQL, paired with a comprehensive UI/UX overhaul of an executive reporting dashboard. The core objective of this project is to transform a cluttered, complex legacy dashboard into a clean, intuitive, and actionable decision-making tool for stakeholders.

## 🛠️ The Challenge: Identifying Dashboard Inefficiencies
An analysis of the initial staging dashboard (`FoodDataDashboard.png`) revealed several critical layout, formatting, and data visualization flaws that increase cognitive load and limit business value:

* **Information Clutter & Text Overlap:** High-level executive KPIs (like Total Revenue) are clipped at the top margin, while chart titles overlap data points, reducing professional polish.
* **Ineffective Chart Selection:** The use of a statistical Box Plot for city sales distribution adds unnecessary complexity for general business stakeholders who simply need quick performance rankings.
* **Visual Overload:** The stacked category bar chart relies on too many granular color slices (individual products), making it nearly impossible to quickly compare product-level performance.
* **Compressed Real Estate:** The bottom-right visual elements (Treemap, Pie Chart, and Legends) are crammed together, causing text collisions and burying regional performance data.

## 🚀 Planned Improvements & UX Design Solutions
To resolve these pain points, the ongoing redesign focuses on data storytelling best practices and dashboard UI/UX frameworks:

* **Establishing Visual Hierarchy:** Relocating core business KPIs (`Total Revenue` and `Total Units Sold`) into dedicated, well-padded cards at the top left to ground the viewer instantly.
* **Simplifying Chart Choices:** Replacing the statistical box plot with a sorted **Horizontal Bar Chart** for city sales to provide an instant performance leaderboard.
* **Streamlining Complex Visuals:** Grouping long-tail product variants into a "Top 10" view or clean category bars, eliminating the hard-to-read multicolor slices.
* **Optimizing Whitespace & Real Estate:** Separating the crowded bottom-right charts, expanding the canvas padding, and adding explicit percentage labels to regional breakdowns so the data can "breathe."
* **Query Optimization:** Refining the underlying data aggregation layers in SQL to ensure the redesigned dashboard loads efficiently.

## 🧰 Tools & Tech Stack
* **SQL:** Data extraction, cleaning, and engineering (see `fooddata.sql`).
* **Data Visualization / BI:** Used for dashboard UI/UX layout and visual reporting.

## 📂 Repository Contents
* `fooddata.sql` - Core SQL queries used for data preparation and aggregation.
* `FoodDataDashboard.png` - Visual interface mockup highlighting the current state and areas flagged for design optimization.
