# Replace values with condition
df.feature_name.loc[(df['feature_name'].isnull())] = 0
df.feature_name.loc[(df['feature_name']=='Dinner')] = 1
df.feature_name.loc[(df['feature_name']=='Lunch')] = 2

# Exclude null, -infinity, infinity from a feature
df_new = df.loc[~((df['feature_name']==np.inf)|(df['feature_name']==-(np.inf))|(df['feature_name'].isnull()))]
