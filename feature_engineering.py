from datavisualization import df

from sklearn import preprocessing

c4 = df

label_encoding = preprocessing.LabelEncoder()
c4['Product ID'] = label_encoding.fit_transform(c4['Product ID'])
c4['Product ID'].unique()
c4['Failure Type'] = label_encoding.fit_transform(c4['Failure Type'])
c4['Type'] = label_encoding.fit_transform(c4['Type'])

c4['Failure Type'].unique()
c4['Type'].unique()

df = c4