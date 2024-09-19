# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = r"C:\Users\pavni\Downloads\Drug safety and pharmacovigilance.csv"
data = pd.read_csv(file_path)

# Step 1: Data Preprocessing
# Check for missing values
print("Missing values in dataset:\n", data.isnull().sum())

# Encode categorical variables (Sex, BP, Cholesterol, Drug)
label_encoder = LabelEncoder()

data['Sex'] = label_encoder.fit_transform(data['Sex'])
data['BP'] = label_encoder.fit_transform(data['BP'])
data['Cholesterol'] = label_encoder.fit_transform(data['Cholesterol'])
data['Drug'] = label_encoder.fit_transform(data['Drug'])

# Step 2: Descriptive Statistics
print("\nDescriptive statistics:\n", data.describe())

# Step 3: Exploratory Data Analysis (EDA)
# Set up visualizations
sns.set(style="whitegrid")

# Age distribution
plt.figure(figsize=(8,6))
sns.histplot(data['Age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Blood Pressure levels vs Na to K Ratio
plt.figure(figsize=(8,6))
sns.boxplot(x='BP', y='Na_to_K', data=data)
plt.title('Blood Pressure vs Na to K Ratio')
plt.xlabel('Blood Pressure Level')
plt.ylabel('Na to K Ratio')
plt.show()

# Cholesterol levels vs Age
plt.figure(figsize=(8,6))
sns.boxplot(x='Cholesterol', y='Age', data=data)
plt.title('Cholesterol Levels vs Age')
plt.xlabel('Cholesterol Level')
plt.ylabel('Age')
plt.show()

# Step 4: Correlation Analysis
# Correlation matrix
corr_matrix = data.corr()
print("\nCorrelation matrix:\n", corr_matrix)

# Heatmap for visualization
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Step 5: Conclusions
# Based on the correlations and visual patterns, we can provide insights into potential
# relationships between demographics and health indicators.
