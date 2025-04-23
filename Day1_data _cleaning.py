import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('retail_feedback_data.csv')
print("📦 Dataset Loaded!\n")
print(df.head())

# Basic info
print("\n📊 Data Info:\n")
print(df.info())

# Check missing values
print("\n❓ Null Values:\n")
print(df.isnull().sum())

# Check duplicates
print("\n🌀 Duplicates:", df.duplicated().sum())

# Basic stats
print("\n📈 Description:\n")
print(df.describe())

# Region-wise order count
sns.countplot(x='Region', data=df)
plt.title('Orders by Region')
plt.show()

# Top products by quantity
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
top_products.plot(kind='barh', title='Top Selling Products')
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product")
plt.show()
