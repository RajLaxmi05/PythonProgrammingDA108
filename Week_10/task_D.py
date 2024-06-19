import matplotlib.pyplot as plt
import pandas as pd 

# Assuming country_data is already defined
country_data = pd.read_csv('WHO-COVID-19-global-data.csv')  # Example of reading the data
df = country_data[['Country', 'Cumulative_cases', 'Cumulative_deaths']]
plt.figure(figsize=(10, 6))
plt.hist(df['Cumulative_cases'], bins=20, color='blue', edgecolor='r')
plt.xlabel('Cumulative COVID-19 Cases')
plt.ylabel('Frequency')
plt.title('Histogram of Cumulative COVID-19 Cases')
plt.grid(True)
plt.show()

