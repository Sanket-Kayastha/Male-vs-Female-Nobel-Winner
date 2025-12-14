import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


data = pd.read_csv("nobel_prize_data.csv")
# print(data)
# print(data.shape)
# print(data.tail())

# print(data.describe())
# print(f"There is any duplicacy: {data.duplicated().values.any()}")
# print(f"To check NaN vlues: {data.isna().values.any()}")
# print(data.isna().sum())
# col_subset = ['year','category', 'laureate_type',
#                 'birth_date','full_name', 'organization_name']
# print(data.loc[data.birth_date.isna()][col_subset])

# print(data.birth_date = pd.to_datetime(data.birth_date))
# print(data.head())
biology = data.sex.value_counts()
# print(biology)

fig = px.pie(labels=biology.index, values=biology.values, title="Percentage of Male vs Female Winners",names=biology.index,hole=0.5)
fig.show()