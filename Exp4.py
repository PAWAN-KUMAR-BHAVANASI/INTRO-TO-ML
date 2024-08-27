import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import tree

# Check the current directory and list files
print("Current Working Directory:", os.getcwd())
print("Files in the current directory:", os.listdir())

# Load data
# If 'data.csv' is in the same directory as this script
df = pd.read_csv("data.csv")

# If 'data.csv' is in a different directory, specify the correct path
# df = pd.read_csv("path/to/your/data.csv")

# Mapping categorical data to numerical values
nationality_map = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(nationality_map)

go_map = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(go_map)

# Define features and target
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

# Initialize and fit the decision tree classifier
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# Plot the decision tree
fig = plt.figure(figsize=(15, 20))
tree.plot_tree(dtree, feature_names=features, filled=True)

# Show the plot
plt.show()

# Display the first few rows of the dataframe
print(df.head())
