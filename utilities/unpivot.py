import argparse
import pandas as pd

# Create the argument parser
parser = argparse.ArgumentParser(description='Unpivot CSV file')
parser.add_argument('-i', '--input', help='Input CSV file', required=True)
parser.add_argument('-f', '--fixed', help='Fixed column', required=True)
args = parser.parse_args()

# Read the input CSV file
df = pd.read_csv(args.input)

if args.fixed is None:
    id_fixed = 1
else:
    id_fixed = args.fixed

# Unpivot the columns
unpivoted_df = pd.melt(df, id_vars=id_fixed, var_name='modalities', 
                       value_name='Value')

# Select only ones 
unpivoted_df = unpivoted_df[unpivoted_df['Value'] == 1].drop(columns=['Value'])

# Sort it and drop 
unpivoted_df = unpivoted_df.sort_values(by='BGGId')

# Save as CSV
unpivoted_df.to_csv("unpivoted_" + input.split("/")[-1], index=False)



