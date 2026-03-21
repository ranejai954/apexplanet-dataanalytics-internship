import pandas as pd

# STEP 1: Load Raw Dataset
df = pd.read_csv("Video Games Sales (1980-2024) - Raw.csv")

print("🔹 First 5 rows:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

# STEP 2: Data Quality Check

print("\n🔹 Missing Values:")
print(df.isnull().sum())

print("\n🔹 Duplicate Rows:")
print(df.duplicated().sum())

print("\n🔹 Statistical Summary:")
print(df.describe())

# STEP 3: Data Cleaning

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values smartly

# Fill categorical columns with 'unknown'
categorical_cols = ['developer', 'publisher']
for col in categorical_cols:
    df[col] = df[col].fillna('unknown')

# Fill numerical columns with 0 (sales data)
sales_cols = ['total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales']
for col in sales_cols:
    df[col] = df[col].fillna(0)

# Fill critic_score with average
df['critic_score'] = df['critic_score'].fillna(df['critic_score'].mean())

# Convert dates properly
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')

# Handle missing values (fill forward)
df = df.fillna(method='ffill')

# Standardize text columns (convert to lowercase if exist)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.lower()

# Convert date column if exists (ignore error if not present)
try:
    df['year'] = pd.to_datetime(df['year'], errors='coerce')
except:
    pass

# STEP 4: Feature Engineering

# Example: Create a new column (if 'year' exists)
if 'year' in df.columns:
    df['release_year'] = df['year']

# Example: Create category based on sales (if exists)
if 'global_sales' in df.columns:
    df['sales_category'] = df['global_sales'].apply(
        lambda x: 'high' if x > 50 else ('medium' if x > 10 else 'low')
    )

# STEP 5: Save Cleaned Dataset

df.to_csv("Video_Games_Sales_Cleaned.csv", index=False)

print("\n✅ Data cleaning completed and saved as 'Video_Games_Sales_Cleaned.csv'")

# Extract release year
df['release_year'] = df['release_date'].dt.year

# Create sales category
df['sales_category'] = df['total_sales'].apply(
    lambda x: 'high' if x > 1 else ('medium' if x > 0.1 else 'low')
)