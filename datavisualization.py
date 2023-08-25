import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
from data_cleaning import df

copy_df3 = df
categ = []
numer = []
for col in copy_df3.columns:
    if df[col].dtypes == object:
        categ.append(col)
    else:
        numer.append(col)

print(categ)
print(numer)


for num in numer:
    plt.subplots(1,1, figsize=(5,5))
    sns.boxplot(copy_df3[num])
    plt.xlabel(num)
plt.show()

# Violin plots.............
for num in numer:
    plt.subplots(1,1, figsize=(5,5))
    sns.violinplot(copy_df3[num])
    plt.xlabel(num)
plt.show()

df = copy_df3
