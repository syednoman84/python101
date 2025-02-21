import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read a CSV file into a DataFrame
df = pd.read_csv("foodhub_order.csv")

# print(df.head().to_string())

# count_not_rated = (df['rating'] == 'Not given').sum()
# print(f"Total Number of Orders With No Rating: {count_not_rated}")

# Select the relevant columns for the pair plot
df_subset = df[['food_preparation_time', 'delivery_time', 'day_of_the_week']]

# Create a pair plot to visualize relationships between preparation time, delivery time, and day of the week
sns.pairplot(df_subset, hue='day_of_the_week')

# Title
plt.suptitle("Pair Plot of Food Preparation Time, Delivery Time, and Day of the Week", y=1.02)
plt.tight_layout()
plt.show()