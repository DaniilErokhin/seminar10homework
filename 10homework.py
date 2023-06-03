import pandas as pd
import seaborn as sns
import google.colab as files
#Задача 1. Найдите, какая область центрального федерального округа имела наибольшую численность студентов вечерней формы обучения в 2015 году
df = pd.read_csv('https://minobrnauki.gov.ru/upload/iblock/6e1/gh0ovqakv5u5srnqutux61mjhx1ilr35.csv', sep = ';', encoding='cp1251')
df

df = pd.read_csv('/content/data20152019.csv', sep = ';', encoding='cp1251')
df = pd.DataFrame(df, columns = ['Субъект РФ', 'Численность студентов очно-заочная (вечерняя) форма, человек, 2015'])
df.iloc[2:19, : 5].max()
df

#Задача 2. Постройте диаграмму с данными о численности студентов дневной формы обучения южного федерального округа за 2017 год.
df = pd.read_csv('/content/data20152019.csv', sep = ';', encoding='cp1251')
df = pd.DataFrame(df, columns = ['Субъект РФ', 'Численность студентов очная форма, человек, 2017'])
df.iloc[33:41, : 7]

plot = sns.barplot(df, x = 'Субъект РФ', y = 'Численность студентов очная форма, человек, 2017')
plot.set_xticklabels(labels = df['Субъект РФ'], rotation = 90)

#Задача 3. Постройте диаграмму количества студентов заочной формы обучения за 2019 год по всем регионам, в которых общее количество студентов не превышает 10000 за данный год.
df = pd.read_csv('/content/data20152019.csv', sep = ';', encoding='cp1251')
df

plot = sns.barplot(df, x = 'Субъект РФ', y = 'Численность студентов очно-заочная (вечерняя) форма, человек, 2019')
plot.set_xticklabels(labels = df['Южный федеральный округ'], rotation = 90)

df = pd.DataFrame(df, columns =['Субъект РФ, Численность студентов очно-заочная (вечерняя) форма, человек, 2019'].between(0, 10000))
df