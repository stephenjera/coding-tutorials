# Global Supersotre Data Analysis

## Easy

* **Total Sales by Region:** What is the total sales amount for each region?
* **Total Sales per Category:** What is the total sales amount for each category?
* **Orders by Country and Ship Mode:** How many orders were shipped for each combination of country and ship_mode?
* **Discount per Sub-Category:** What is the average discount percentage given for each product sub-category?
* **Total Profits per Customer:**  What are the total profits per customer?

## Medium

* **Ranked Top Selling Products by Category:** Assign a rank to the top selling products by category
* **High-Value Customers:** For each customer, find the total number of orders and the total sales amount, but only include customers who have placed more than 10 orders and have a total sales amount greater than $10,000.
* **Running Total of Sales:** Calculate the running total of sales for each customer, ordered by the order_date. (Requires window function)
* **Top Products by Profit:** Find the top 3 products with the highest total profit in each region, and include the product name, category, and total profit for those products. (Requires subquery, aggregation, and ranking)

## Hard

* **Order Processing Time:** For each order, calculate the difference between the ship_date and order_date. Then, find the average and maximum of these differences, grouped by the combination of region, order_priority, and ship_mode. However, only include combinations where the maximum difference is greater than 5 days.
* **Multi-Region Customers:** Identify customers who have made orders in multiple regions, and for each of those customers, find the region where they made the most orders and the region where they had the highest total sales amount.
* **Year-over-Year Growth Rate:** Calculate the year-over-year growth rate of sales for each product category, comparing the total sales for each category between the current year and the previous year.
