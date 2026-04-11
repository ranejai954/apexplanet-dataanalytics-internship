-- Task 2: SQL Queries for Data Analysis

-- 1. Top 5 Games by Total Sales
SELECT title, total_sales
FROM video_games
ORDER BY total_sales DESC
LIMIT 5;

-- 2. Total Sales by Genre
SELECT genre, SUM(total_sales) AS total_sales
FROM video_games
GROUP BY genre
ORDER BY total_sales DESC;

-- 3. Top 10 Platforms by Sales
SELECT console, SUM(total_sales) AS total_sales
FROM video_games
GROUP BY console
ORDER BY total_sales DESC
LIMIT 10;

-- 4. Average Critic Score by Genre
SELECT genre, AVG(critic_score) AS avg_score
FROM video_games
GROUP BY genre
ORDER BY avg_score DESC;

