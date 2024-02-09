import pandas as pd

try:
    df1 = pd.read_csv('df1.csv')
    df2 = pd.read_csv('df2.csv')

    diff2 = df1.merge(df2,indicator=True, how ='outer').loc[lambda v: v['_merge'] != 'both']

    # Drop the '_merge' column
    diff2.drop(columns=['_merge'], inplace=True)

    # Export unmatched results to a CSV file
    diff2.to_csv('unmatched_results.csv', index=False)

except FileNotFoundError:
    print("One or both of the input CSV files not found.")
except pd.errors.EmptyDataError:
    print("One or both of the input CSV files are empty.")
