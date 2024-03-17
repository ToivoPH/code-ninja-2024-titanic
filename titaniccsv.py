import pandas as pd

print('running')

df = pd.read_csv("titanic_cleaned.csv")

df.iloc[1:3]
#iloc is rows then columns (:,:)

#df[df['Age'] <= 16]
"""
import seaborn as sns
import matplotlib.pyplot as plt
#loading data
titanic = pd.read_csv('titanic_cleaned.csv')
#Countplot
sns.catplot(x ="Sex", hue ="Survived", kind ="count", data = titanic)
plt.show()
plt.savefig('demotitanic.png') #save this graphic to your computer
"""

#task 1
"""
df[['Sex', 'Fare']].groupby('Sex').sum()
"""

#task 2
"""import matplotlib.pyplot as plt
titanic = pd.read_csv('titanic_cleaned.csv')

bins = [0, 16, 60, df['Age'].max()]
#print(bins)
labels = ['under 16', 'between 16 and 60', 'over 60']
df['Age_category'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
#print(df['Age_category'])
category_count = df['Age_category'].value_counts()
print(category_count)
plt.pie(category_count, explode=(0, 0.1, 0), labels=category_count.index, autopct='%1.2f%%', startangle=90)
plt.show()
plt.savefig('demopieagetitanic.png')
"""

#task 3 
#what are the chances of a child surviving

under_30 = df[df['Age'] < 30]

psurvive =  len(under_30) / len(df)
print(f"{psurvive * 100}%")