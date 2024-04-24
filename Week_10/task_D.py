import matplotlib.pyplot as plt
df = country_data[['Country', 'Cumulative_cases', 'Cumulative_deaths']]
plt.figure(figsize=(10, 6))
plt.hist(df['Cumulative_cases'], bins=20, color='blue', edgecolor='r')
plt.xlabel('Cumulative COVID-19 Cases')
plt.ylabel('Frequency')
plt.title('Histogram of Cumulative COVID-19 Cases')
plt.grid(True)
plt.show()
