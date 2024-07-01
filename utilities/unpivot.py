import argparse
import pandas as pd

# Create the argument parser
parser = argparse.ArgumentParser(description='Unpivot CSV file')
parser.add_argument('-i', '--input', help='Input CSV file', required=True)
parser.add_argument('-f', '--fixed', help='Fixed column', required=True)
args = parser.parse_args()


args.input = "/home/gguex/OneDrive/cours_database/datasets/board_games/mechanics.csv"

# Read the input CSV file
df = pd.read_csv(args.input)

# Unpivot the columns
unpivoted_df = pd.melt(df, id_vars=[args.fixed], var_name='Column', value_name='Value')

# Print the unpivoted dataframe
print(unpivoted_df)