import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load your dataset
data = pd.read_csv("smartphones.csv")

# Create a directory to save visualizations
if not os.path.exists("visualizations"):
    os.makedirs("visualizations")

# Visualization 1: Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['column1'], kde=True)
plt.title('Histogram of Column 1')
plt.savefig("visualizations/histogram_column1.png")
plt.close()

# Visualization 2: Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='column1', y='column2', data=data)
plt.title('Scatter Plot between Column 1 and Column 2')
plt.savefig("visualizations/scatterplot_column1_column2.png")
plt.close()

# Visualization 3: Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='column3', y='column4', data=data)
plt.title('Box Plot between Column 3 and Column 4')
plt.savefig("visualizations/boxplot_column3_column4.png")
plt.close()

# Visualization 4: Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='column5', y='column6', data=data)
plt.title('Bar Plot between Column 5 and Column 6')
plt.savefig("visualizations/barplot_column5_column6.png")
plt.close()

# Visualization 5: Scatter Plot for another pair of columns
plt.figure(figsize=(10, 6))
sns.scatterplot(x='column3', y='column5', data=data)
plt.title('Scatter Plot between Column 3 and Column 5')
plt.savefig("visualizations/scatterplot_column3_column5.png")
plt.close()

# Visualization 6: Scatter Plot for another pair of columns
plt.figure(figsize=(10, 6))
sns.scatterplot(x='column2', y='column4', data=data)
plt.title('Scatter Plot between Column 2 and Column 4')
plt.savefig("visualizations/scatterplot_column2_column4.png")
plt.close()

# Visualization 7: Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap of Correlation Matrix')
plt.savefig("visualizations/heatmap_correlation_matrix.png")
plt.close()

# Generate more visualizations here...

print("Visualizations generated successfully.")
