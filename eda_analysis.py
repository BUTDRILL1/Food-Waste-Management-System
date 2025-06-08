# eda_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("PGADMIN_USER")
password = os.getenv("PGADMIN_PASSWORD")
db_url = f"postgresql://{user}:{password}@localhost:5432/food_waste_management"
engine = create_engine(db_url)

# --- Load Data ---
providers = pd.read_sql("SELECT * FROM providers", engine)
receivers = pd.read_sql("SELECT * FROM receivers", engine)
food = pd.read_sql("SELECT * FROM food_listings", engine)
claims = pd.read_sql("SELECT * FROM claims", engine)

# --- Basic Info ---
print("=== Data Shapes ===")
print("Providers:", providers.shape)
print("Receivers:", receivers.shape)
print("Food Listings:", food.shape)
print("Claims:", claims.shape)

print("\n=== Null Values ===")
print(food.isnull().sum())

print("\n=== Data Types ===")
print(food.dtypes)

# --- Descriptive Stats ---
print("\n=== Food Quantity Stats ===")
print(food['quantity'].describe())

# --- Visualizations ---
import warnings
warnings.filterwarnings("ignore")
sns.set(style="whitegrid")

# 1. Quantity distribution
plt.figure(figsize=(8,4))
sns.histplot(food['quantity'], bins=20, kde=True)
plt.title("Distribution of Food Quantity")
plt.xlabel("Quantity")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plots/quantity_distribution.png")
plt.close()

# 2. Meal Type counts
plt.figure(figsize=(6,4))
sns.countplot(data=food, x='meal_type', order=food['meal_type'].value_counts().index)
plt.title("Meal Type Distribution")
plt.tight_layout()
plt.savefig("plots/meal_type_distribution.png")
plt.close()

# 3. Food Type counts
plt.figure(figsize=(6,4))
sns.countplot(data=food, x='food_type', order=food['food_type'].value_counts().index)
plt.title("Food Type Distribution")
plt.tight_layout()
plt.savefig("plots/food_type_distribution.png")
plt.close()

# 4. Claims status
plt.figure(figsize=(6,4))
sns.countplot(data=claims, x='status', order=claims['status'].value_counts().index)
plt.title("Claims Status Overview")
plt.tight_layout()
plt.savefig("plots/claims_status.png")
plt.close()

# 5. Correlation (claims + food quantities)
merged = claims.merge(food, on='food_id', how='left')

if not merged.empty:
    corr = merged[['quantity']].corr()
    print("\n=== Correlation Matrix ===")
    print(corr)
else:
    print("\nMerged DataFrame is empty. Skipping correlation analysis.")

print("\nEDA completed. Plots saved in 'plots/' folder.")
