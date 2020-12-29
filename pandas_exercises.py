import pandas as pd
df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'C'],
                   'points': [25, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 9, 12],
                   'rebounds': [11, 8, 10, 6, 6]})
print('Dataframe')
print(df)

print('\nReturn only rows where points > 13 AND assists > 7')
print(df[(df.points > 13) & (df.assists > 7)])

print('\nReturn only rows where points > 13 OR assists > 7')
print(df[(df.points > 13) | (df.assists > 7)])

print('\nReturn only rows where team is A or points >= 15')
print(df[(df.team == 'A') | (df.points >= 15)])

# Define a list of values
filter_list = [12, 14, 15]
print('\nPoints-Filter List =', filter_list)
# Return only rows where points is in the list of values
print(df[df.points.isin(filter_list)])

#  Filtering on Three Conditions
print(df[(df.team == 'B') & (df.points >= 12) & (df.assists > 7)])
