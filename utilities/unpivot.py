import argparse
import pandas as pd

# Create the argument parser
parser = argparse.ArgumentParser(description='Unpivot CSV file')
parser.add_argument('-i', '--input', help='Input CSV file', required=True)
parser.add_argument('-f', '--fixed', help='Fixed column')
args = parser.parse_args()

# Read the input CSV file
df = pd.read_csv(args.input)

if args.fixed is None:
    df.insert(0, "id", range(1, len(df)+1))
    args.fixed = "id"

# Unpivot the columns
unpivoted_df = pd.melt(df, id_vars=args.fixed, var_name='modalities', 
                       value_name='Value')

# Select only ones and drop value
unpivoted_df = unpivoted_df[unpivoted_df['Value'] == 1].drop(columns=['Value'])

# Sort it 
unpivoted_df = unpivoted_df.sort_values(by=args.fixed)

# Save as CSV
unpivoted_df.to_csv("unpivoted_" + args.input.split("/")[-1], index=False)