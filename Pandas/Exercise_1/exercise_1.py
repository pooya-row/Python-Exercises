import pandas as pd


pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# 1
with open('data.csv', 'r') as f:
    df = pd.read_csv(f, delimiter='|')


# print(df.iloc[2])
# 2
# print(df.info())
# print(df.columns)

# 3
# with open('tab_del.csv', 'w') as f:
#     df.to_csv(f, sep='\t', index=False, line_terminator='\n')

# 4
print(df['OCCUPATION'])

# 5
# print(df.iloc[10:21])

# 6
# import re
# trans_col = []
# for col in df.columns:
#     if (re.findall(r'\w*TRANSACTION\w*', col)) != []:
#         trans_col.append(col)
# better solution:
# col = [col for col in df.columns if col.startswith('TRANSACTION')]
# trans_df = df[trans_col]
# print(trans_df)

# 7
# print(df[df['CITY'] == 'BIRMINGHAM'])

# 8
# print(df['CITY'].value_counts()['BIRMINGHAM'])

# 9
# print(df[df['CITY']=='BIRMINGHAM']['OCCUPATION'])

# 10
# print(df['CITY'].nunique(), '\n')
# print(df['CITY'].unique())

# 11
# print(df.sort_values(by='TRANSACTION_DT')) # zero null

# 12
print(len(df[(df['CITY'] == 'BIRMINGHAM') &
             (df['TRANSACTION_AMT'] > 500)].index))

# 13
# print(df['STATE'].unique())

# 14
# df['FULL_NAME'] = str(df['FIRST_NAME']) + " " + str(df['LAST_NAME'])
# print(df['FULL_NAME'])

# 15
# df['RICH'] = df['TRANSACTION_AMT'] > 5000

# 16
# df['TRANSACTION_DT'].apply(print)

# 17
# def data_split(x):
#     return list(map(str, x.split('-')))
#
#
# print(df['TRANSACTION_DT'].apply(data_split))
# BETTER
# print(df['TRANSACTION_DT'].apply(lambda x: x.split('-')))


# 18
# def year_split(x):
#     return list(map(str, x.split('-')))[0]
#
#
# df['YEAR'] = df['TRANSACTION_DT'].apply(year_split)
# even better:
df['YEAR'] = df['TRANSACTION_DT'].apply(lambda x: x.split('-')[0])
print(df.head())

# 19
# jj = df.groupby('CITY').groups
# for k, v in jj.items():
#     print(k + ':\t' + str(len(v)))
# print(df['CITY'].value_counts(sort=False))  # alternative


# 20
# gg = df['CITY'].value_counts(sort=False)
# new_df = pd.DataFrame(list(zip(list(gg.index), list(gg.values))),
#                       columns=['CITY', 'COUNT'])
# new_df.sort_values(['COUNT'], ascending=False, inplace=True)

# # better
# new_df = pd.DataFrame(df.groupby('CITY').count()['id'])
# new_df.reset_index(inplace=True)
# new_df.columns = ['CITY', 'COUNT']
# new_df.sort_values(['COUNT'], ascending=False, inplace=True)
#
# with open('counts.csv', 'w') as f:
#     new_df.to_csv(f, sep='\t', index=False, line_terminator='\n')
