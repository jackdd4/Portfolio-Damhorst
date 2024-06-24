-- Research Questions
-- Q1: What are the total sales this year?
-- Q2: Which cities generate the most sales?
-- Q3: What products are pruchased the most per city?
-- Q4: What is the top selling product per city?
-- Q5: What month generated the most revenue?
-- Q6: What type of cookie was sold the most each month in Q4?
-- Q7: What are the sales trends for different categories over the past year?
-- Q8: What is the average unit price by category?
-- Q9: What is the Price/Quantity Ratio across regions?
-- Q10: What were the highest value transactions?
-- Q11: What were the total quantities sold of each product?

-- Q1: What are the total sales this year?

USE prim;
SELECT YEAR(Date) AS Year, SUM(TotalPrice) AS TotalSales
FROM fooddata
GROUP BY YEAR(Date);

-- Q2: Which cities generate the most sales?

SELECT City, SUM(TotalPrice) AS TotalSales
FROM fooddata
GROUP BY City
ORDER BY TotalSales DESC;

-- Q3: What products are pruchased the most per city?

SELECT City, Category, Product, SUM(TotalPurchases) AS TotalSales
FROM (
    SELECT City, Category, Product, COUNT(Product) AS TotalPurchases
    FROM fooddata
    GROUP BY City, Category, Product
) AS purchases_per_city_category_product
GROUP BY City, Category, Product
ORDER BY City, Category, TotalSales DESC;

-- Q4: What is the top selling product per city?

SELECT City, Category, Product, TotalPurchases
FROM (
    SELECT City, Category, Product, COUNT(Product) AS TotalPurchases
    FROM fooddata
    GROUP BY City, Category, Product
) AS purchases_per_city
WHERE (City, TotalPurchases) IN (
    SELECT City, MAX(TotalPurchases)
    FROM (
		SELECT City, COUNT(Product) AS TotalPurchases
        FROM fooddata
        GROUP BY City, Category, Product
    ) AS max_purchases_per_city
    GROUP BY City
);

-- Q5: What month generated the most revenue?

SELECT Month, SUM(TotalPrice) AS Earnings
FROM fooddata
GROUP BY Month
ORDER BY Earnings DESC;

-- Q6: What type of cookie was sold the most each month in Q4?

SELECT Month, Product, SUM(QTY) AS QTY
FROM fooddata
WHERE Month in ('Oct', 'Nov', 'Dec')
AND Category = 'Cookies'
GROUP BY Month, Product
ORDER BY QTY DESC;

-- Q7: What are the sales trends for different categories over the past year?

SELECT Month, Category, SUM(TotalPrice) as TotalSales 
FROM fooddata
GROUP BY Month, Category
ORDER BY Month, Category; 

-- Q8: What is the average unit price by category?

SELECT Category, AVG(UnitPrice) AS AvgUnitPrice
FROM fooddata
GROUP BY Category;

-- Q9: What is the Price/Quantity Ratio across regions?

SELECT Region, SUM(TotalPrice) / SUM(Qty) AS SalesEfficiency
FROM fooddata
GROUP BY Region;

-- Q10: What were the highest value transactions?

SELECT *
FROM fooddata
ORDER BY TotalPrice DESC
LIMIT 10;

-- Q11: What were the total quantities sold of each product?

SELECT Product, Category, SUM(Qty) AS Total_Qty
FROM fooddata
GROUP BY Product, Category
ORDER BY Total_Qty DESC;

