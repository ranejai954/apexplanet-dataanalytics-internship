# Task 2: Exploratory Data Analysis (EDA)

import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load Cleaned Dataset
df = pd.read_csv("Video_Games_Sales_Cleaned.csv")

print("🔹 First 5 rows:")
print(df.head())

# STEP 2: Basic Analysis

print("\n🔹 Average Sales:")
print(df['total_sales'].mean())

print("\n🔹 Top Genres:")
print(df['genre'].value_counts().head())

# STEP 3: Top Games by Sales

top_games = df.sort_values(by='total_sales', ascending=False).head(10)

print("\n🔹 Top 10 Games by Sales:")
print(top_games[['title', 'total_sales']])

# STEP 4: Sales by Genre

genre_sales = df.groupby('genre')['total_sales'].sum().sort_values(ascending=False)

print("\n🔹 Sales by Genre:")
print(genre_sales)

# STEP 5: Sales by Platform

platform_sales = df.groupby('console')['total_sales'].sum().sort_values(ascending=False).head(10)

print("\n🔹 Top Platforms by Sales:")
print(platform_sales)



# STEP 6: VISUALIZATIONS

# 1. Top Genres Bar Chart
genre_sales.head(10).plot(kind='bar')
plt.title("Top Genres by Sales")
plt.xlabel("Genre")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Sales Distribution Histogram
df['total_sales'].plot(kind='hist', bins=30)
plt.title("Sales Distribution")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.show()

# 3. Critic Score vs Sales Scatter Plot
plt.scatter(df['critic_score'], df['total_sales'])
plt.xlabel("Critic Score")
plt.ylabel("Total Sales")
plt.title("Critic Score vs Sales")
plt.tight_layout()
plt.show()

print("\n✅ Task 2 Analysis Completed!")