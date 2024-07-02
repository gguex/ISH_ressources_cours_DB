import pandas as pd

# Define the input and output file
folder_path = "/home/gguex/OneDrive/cours_database/datasets/board_games/"
input_file = "user_ratings.csv"
output_file = "sampled_user_ratings.csv"

# Read the input CSV file
df = pd.read_csv(folder_path + input_file)

# Count the number of ratings per user
ratings_per_user = df["Username"].value_counts()

# Select the 30 users with the most ratings
selected_users = ratings_per_user.head(50).index

# Filter the dataframe
sampled_df = df[df["Username"].isin(selected_users)]

# Save as CSV
sampled_df.to_csv(folder_path + output_file, index=False)