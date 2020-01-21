# Replace values with condition
df.feature_name.loc[(df['feature_name'].isnull())] = 0
df.feature_name.loc[(df['feature_name']=='Dinner')] = 1
df.feature_name.loc[(df['feature_name']=='Lunch')] = 2
