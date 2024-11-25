import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('cars.csv')

# Basic summary of dataset
print("Data Info:\n", df.info())
print("\nSummary Statistics:\n", df.describe())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Price distribution
sns.histplot(df['Price'], kde=True)
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Boxplot of prices by car make
plt.figure(figsize=(12, 6))
sns.boxplot(x='Make', y='Price', data=df)
plt.xticks(rotation=45)
plt.title('Car Prices by Make')
plt.show()

# Scatter plot of Engine Size vs MPG
sns.scatterplot(x='Engine Size', y='MPG', data=df)
plt.title('Engine Size vs MPG')
plt.xlabel('Engine Size (L)')
plt.ylabel('Miles Per Gallon (MPG)')
plt.show()
