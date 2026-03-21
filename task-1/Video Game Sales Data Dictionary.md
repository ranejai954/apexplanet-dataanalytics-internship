📄 📊 DATA DICTIONARY — Video Game Sales Dataset

1. img
Meaning: URL or path of the game’s cover image
Data Type: Object (String)

Description: Used for visual representation; not useful for analysis
2. title
Meaning: Name of the video game
Data Type: Object (String)
Description: Identifies each game

3. console
Meaning: Platform on which the game is released (e.g., PS4, Xbox)
Data Type: Object (String)
Description: Helps analyze platform-wise performance

4. genre
Meaning: Category/type of the game (e.g., Action, Sports)
Data Type: Object (String)
Description: Useful for genre-based analysis

5. publisher
Meaning: Company that published the game
Data Type: Object (String)
Description: Helps identify top publishers

6. developer
Meaning: Company that developed the game
Data Type: Object (String)
Description: Some values were missing and handled during cleaning

7. critic_score
Meaning: Rating given by critics (scale typically 1–10)
Data Type: Float
Description: Missing values replaced with mean score

8. total_sales
Meaning: Total global sales of the game (in millions)
Data Type: Float
Description: Key metric for overall performance

9. na_sales
Meaning: Sales in North America (in millions)
Data Type: Float
Description: Regional sales data

10. jp_sales
Meaning: Sales in Japan (in millions)
Data Type: Float
Description: Regional sales data

11. pal_sales
Meaning: Sales in PAL regions (Europe, etc.)
Data Type: Float
Description: Regional sales data

12. other_sales
Meaning: Sales in other regions (in millions)
Data Type: Float
Description: Remaining global sales

13. release_date
Meaning: Date when the game was released
Data Type: DateTime
Description: Converted from string to datetime format

14. last_update
Meaning: Last update date of the dataset entry
Data Type: DateTime
Description: Contains many missing values

15. release_year (Created Column)
Meaning: Year extracted from release_date
Data Type: Integer
Description: Created during feature engineering

16. sales_category (Created Column)
Meaning: Categorization of games based on total sales
Data Type: Object (String)
Categories:
High → Sales > 1
Medium → Sales between 0.1 and 1
Low → Sales < 0.1
Description: Helps in grouping games by performance