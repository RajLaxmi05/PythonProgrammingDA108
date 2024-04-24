import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("WHO-COVID-19-global-data.csv")

data['Date_reported'] = pd.to_datetime(data['Date_reported'])
data['Days_since'] = (data['Date_reported'] - pd.Timestamp('2020-01-03')).dt.days
india_data = data[data['Country'] == 'India']
us_data = data[data['Country'] == 'United States of America']
brazil_data = data[data['Country'] == 'Brazil']

plt.figure(figsize=(10, 6))
plt.plot(data['Days_since'], data['New_cases'], label='Global', color='blue')
plt.plot(india_data['Days_since'], india_data['New_cases'], label='India', color='green')
plt.plot(us_data['Days_since'], us_data['New_cases'], label='US', color='red')
plt.plot(brazil_data['Days_since'], brazil_data['New_cases'], label='Brazil', color='orange')
plt.xlabel('Days since 2020-01-03')
plt.ylabel('New Cases')
plt.title('Global COVID-19 New Case Count')
plt.legend()
plt.grid(True)
# Change y-axis scale to linear instead of scientific notation
plt.ticklabel_format(style='plain', axis='y')
plt.show()
