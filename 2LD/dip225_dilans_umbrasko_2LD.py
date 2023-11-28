import pandas as pd

get_info = input()

fails = pd.read_excel('2LD/description1.xlsx', sheet_name='LookupAREA')

filtered_df = fails[fails[1] == get_info]

reg_name = filtered_df.iloc[0, 0]

region = []

with open('2LD/data.csv', 'r') as f:
    next(f)  # Skip header
    for line in f:
        row = line.rstrip().split(',')
        if row[1] == reg_name:
            region.append(int(row[3]))

print(sum(region))
