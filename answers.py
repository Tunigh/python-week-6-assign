import pandas as pd

# Load the dataset
df = pd.read_csv('iris.csv')

# Display the first few rows of the dataset
print(df.head())

# Explore the structure of the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Clean the dataset by filling missing values with the mean of the column
df.fillna(df.mean(), inplace=True)

# Display the cleaned dataset
print(df.head())

# Load the dataset
df = pd.read_csv('sales.csv')

# Compute the basic statistics of the numerical columns
print(df.describe())

# Perform groupings on a categorical column and compute the mean of a numerical column for each group
grouped = df.groupby('region')
sales_mean = grouped['sales'].mean()

# Display the results
print(sales_mean)
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris = pd.read_csv('iris.csv')

# Line chart showing trends over time (for example, a time-series of sales data)
plt.figure(figsize=(10, 6))
plt.plot(iris['sepal_length'], iris['sepal_width'], label='Sepal Length vs Width')
plt.title('Trend of Sepal Length and Width Over Time')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()

# Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species)
plt.figure(figsize=(10, 6))
plt.bar(iris['species'], iris['petal_length'].mean(), label='Average Petal Length per Species')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# Histogram of a numerical column to understand its distribution
plt.figure(figsize=(10, 6))
plt.hist(iris['petal_length'], bins=10, edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length)
plt.figure(figsize=(10, 6))
plt.scatter(iris['sepal_length'], iris['petal_length'], color='blue', edgecolor='black')
plt.title('Relationship between Sepal Length and Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()