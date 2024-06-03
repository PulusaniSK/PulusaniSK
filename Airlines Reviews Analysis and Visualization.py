import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Airlines Reviews DataSet.csv'
airlines_reviews = pd.read_csv(file_path)

# Dropping unnecessary columns
columns_to_drop = ['Column1']
airlines_reviews_cleaned = airlines_reviews.drop(columns=columns_to_drop)

# Handling missing values
# For simplicity, we'll fill numerical columns with the mean and categorical columns with the mode
for column in airlines_reviews_cleaned.select_dtypes(include=['float64', 'int64']).columns:
    airlines_reviews_cleaned[column].fillna(airlines_reviews_cleaned[column].mean(), inplace=True)

for column in airlines_reviews_cleaned.select_dtypes(include=['object']).columns:
    airlines_reviews_cleaned[column].fillna(airlines_reviews_cleaned[column].mode()[0], inplace=True)

# Descriptive statistics
descriptive_stats = airlines_reviews_cleaned.describe(include='all')

# Set up the plotting style
sns.set(style="whitegrid")

# Create subplots for the distribution of ratings
fig, axes = plt.subplots(3, 2, figsize=(14, 18))

# List of rating columns
rating_columns = ['Seat Comfort', 'Cabin Staff Service', 'Ground Service', 
                  'Food & Beverages', 'Wifi & Connectivity', 'Inflight Entertainment']

# Plot histograms for each rating column
for ax, column in zip(axes.flatten(), rating_columns):
    sns.histplot(airlines_reviews_cleaned[column], bins=10, kde=True, ax=ax)
    ax.set_title(f'Distribution of {column}')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# Pie chart for the recommendation breakdown
recommendation_counts = airlines_reviews_cleaned['Recommended'].value_counts()
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(recommendation_counts, labels=recommendation_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightgreen'])
ax.set_title('Recommendation Breakdown')
plt.show()

# Boxplots for ratings by Seat Type
fig, axes = plt.subplots(3, 2, figsize=(14, 18))
seat_types = airlines_reviews_cleaned['Seat_Types'].unique()

for ax, column in zip(axes.flatten(), rating_columns):
    sns.boxplot(x='Seat_Types', y=column, data=airlines_reviews_cleaned, ax=ax, palette="Set3")
    ax.set_title(f'{column} by Seat Type')
    ax.set_xlabel('Seat Type')
    ax.set_ylabel('Rating')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

plt.tight_layout()
plt.show()

# Boxplots for ratings by Traveler Type
fig, axes = plt.subplots(3, 2, figsize=(14, 18))
traveler_types = airlines_reviews_cleaned['Type_of_Travellers'].unique()

for ax, column in zip(axes.flatten(), rating_columns):
    sns.boxplot(x='Type_of_Travellers', y=column, data=airlines_reviews_cleaned, ax=ax, palette="Set2")
    ax.set_title(f'{column} by Traveler Type')
    ax.set_xlabel('Traveler Type')
    ax.set_ylabel('Rating')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

plt.tight_layout()
plt.show()
