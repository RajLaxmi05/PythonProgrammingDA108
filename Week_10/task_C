import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("WHO-COVID-19-global-data.csv")

# Group data by country and calculate cumulative case count and death count
country_data = data.groupby('Country').agg({'Cumulative_cases': 'max', 'Cumulative_deaths': 'max'}).reset_index()
# Create a DataFrame with required columns
df = country_data[['Country', 'Cumulative_cases', 'Cumulative_deaths']]

# Plot scatter plot of cumulative case count vs cumulative death count
plt.figure(figsize=(10, 6))
plt.scatter(df['Cumulative_cases'], df['Cumulative_deaths'], color = 'blue')
plt.xlabel('Cumulative COVID case count')
plt.ylabel('Cumulative COVID death count')
plt.title('Cumulative COVID cases count vs Cumulative COVID deaths count')
plt.grid(True)
plt.show()






top_five_countries = df.nlargest(5, 'Cumulative_cases')
plt.figure(figsize=(10, 6))
plt.bar(top_five_countries['Country'], top_five_countries['Cumulative_cases'], color = 'r')
plt.xlabel('Country')
plt.ylabel('Cumulative COVID Case Count')
plt.title('Top Five Countries by Cumulative COVID Case Count')
# plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
