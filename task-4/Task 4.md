# Task 4: Data Storytelling and Hypothesis Testing

This task focuses on transforming data analysis into a structured story and validating insights using statistical methods. The goal was to combine analytical thinking with data storytelling to present meaningful and actionable conclusions.

## Objective
The primary objective of this task was to analyze video game sales data, identify key patterns, and present findings through a clear narrative supported by statistical testing.

## Data Storytelling
The analysis revealed several important trends in the dataset. The Sports genre emerged as the highest-selling category, indicating strong market demand. Similarly, the PS2 platform dominated overall sales, highlighting the importance of platform reach and popularity.

Sales trends over time showed fluctuations rather than consistent growth, suggesting that external factors such as market conditions, release timing, and platform cycles influence performance. Additionally, most games contributed to low sales, indicating a long-tail distribution in the dataset.

## Hypothesis Testing
A hypothesis was formulated to test whether critic scores have an impact on total sales:

**Hypothesis:** Games with higher critic scores tend to achieve higher total sales.

To evaluate this, a Pearson correlation test was performed between critic_score and total_sales after removing missing values.

## Results
The correlation coefficient was found to be 0.14, indicating a very weak positive relationship. The p-value was less than 0.05, suggesting that the relationship is statistically significant.

## Interpretation
Although a statistically significant relationship exists, the strength of the correlation is very weak. This indicates that critic scores have only a minimal influence on total sales.

## Conclusion
The hypothesis is only partially supported. While higher critic scores are slightly associated with increased sales, they are not a strong predictor of commercial success. Other factors such as marketing strategies, platform popularity, and genre selection play a more significant role in determining sales performance.

## Key Learnings
- Data storytelling helps in communicating insights effectively  
- Statistical testing validates assumptions with evidence  
- Business decisions should rely on multiple factors, not a single metric  
- Visualization enhances understanding of complex data  

This task demonstrates how data analysis, storytelling, and statistical methods can be combined to derive meaningful insights and support data-driven decision-making.