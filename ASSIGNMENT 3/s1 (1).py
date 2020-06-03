#importing library files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#retriving data
csv ='https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv'
df = pd.read_csv(csv)
print(df)
df1 = df.pivot_table(index='continent',
                     columns='year',
                     values='lifeExp')
#saving heat map
sns.heatmap(df1,annot=True).get_figure().savefig("heatMap.png")

