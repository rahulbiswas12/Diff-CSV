import pandas as pd

try:
    df1 = pd.read_csv('df1.csv')
    df2 = pd.read_csv('df2.csv')
'''
# Method1 : isin function/method
    diff = df1[~df1.apply(tuple, 1).isin(df2.apply(tuple, 1))]
    print(diff)
'''
# Method2: Merge
    diff2 = df1.merge(df2,indicator=True, how ='outer').loc[lambda v: v['_merge'] != 'both']

    # Drop the '_merge' column
    diff2.drop(columns=['_merge'], inplace=True)

    # Export unmatched results to a CSV file
    diff2.to_csv('unmatched_results.csv', index=False)

except FileNotFoundError:
    print("One or both of the input CSV files not found.")
except pd.errors.EmptyDataError:
    print("One or both of the input CSV files are empty.")
