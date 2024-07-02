import argparse
import pandas as pd

# Create the argument parser
parser = argparse.ArgumentParser(description='Unpivot CSV file')
parser.add_argument('-i', '--input', help='Input CSV file', required=True)
parser.add_argument('-f', '--fixed', help='Fixed column')
parser.add_argument('-b', '--binary', help='Binary values, keep only ones', 
                    action='store_true')
parser.add_argument('-r', '--remove', help='Remove zero values', 
                    action='store_true')
args = parser.parse_args()

# Read the input CSV file
df = pd.read_csv(args.input)

if args.fixed is None:
    df.insert(0, "id", range(1, len(df)+1))
    args.fixed = "id"

# Unpivot the columns
unpivoted_df = pd.melt(df, id_vars=args.fixed, var_name='modalities', 
                       value_name='values')

# Select only ones and drop value if -b is true
if args.binary:
    unpivoted_df = \
        unpivoted_df[unpivoted_df['values'] > 0].drop(columns=['values'])

# Remove zero values
if args.remove:
    unpivoted_df = unpivoted_df[unpivoted_df['values'] > 0]

# Sort it 
unpivoted_df = unpivoted_df.sort_values(by=[args.fixed, 'modalities'])

# Save as CSV
unpivoted_df.to_csv("unpivoted_" + args.input.split("/")[-1], index=False)