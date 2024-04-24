import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("WHO-COVID-19-global-data.csv")

india_data = data[data['Country'] == 'India']
brazil_data = data[data['Country'] == 'Brazil']

plt.figure(figsize=(8, 6))
plt.scatter(india_data['Date_reported'], india_data['New_cases'], label='India', color='blue')
plt.scatter(brazil_data['Date_reported'], brazil_data['New_cases'], label='Brazil', color='red')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.title('Daily COVID-19 New Case Count: India vs Brazil')
plt.legend()
# plt.grid(True)
plt.show()








plt.figure(figsize=(8, 6))
plt.scatter(data['New_cases'], data['Cumulative_deaths'], color='orange')
plt.xlabel('New Cases')
plt.ylabel('Cumulative Deaths')
plt.title('Scatter Plot: Global New Cases vs Cumulative Deaths')
plt.show()








data['Date_reported'] = pd.to_datetime(data['Date_reported'])
data_2020 = data[data['Date_reported'].dt.year == 2020]
data_2021 = data[data['Date_reported'].dt.year == 2021]
data_2022 = data[data['Date_reported'].dt.year == 2022]

plt.figure(figsize=(18,6))

plt.subplot(1, 3, 1)
plt.scatter(data_2020['New_cases'], data_2020['Cumulative_deaths'], color='blue')
plt.xlabel("New Cases")
plt.ylabel('Cumulative Deaths')
plt.title('2020')

plt.subplot(1, 3, 2)
plt.scatter(data_2021['New_cases'], data_2021['Cumulative_deaths'], color='green')
plt.xlabel("New Cases")
plt.ylabel('Cumulative Deaths')
plt.title('2021')

plt.subplot(1, 3, 3)
plt.scatter(data_2022['New_cases'], data_2022['Cumulative_deaths'], color='red')
plt.xlabel("New Cases")
plt.ylabel('Cumulative Deaths')
plt.title('2022')

plt.show()
