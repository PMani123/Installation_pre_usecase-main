from data_analysis import df

c2 = df
c2['Product ID'].unique()
c2.dropna()

c2.fillna(0, inplace = True)

df = c2