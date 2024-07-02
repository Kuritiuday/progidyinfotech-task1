import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:/Users/kurit/OneDrive/Desktop/progidy infotech/API_SP.POP.TOTL_DS2_en_csv_v2_477290.csv'
data = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_477290.csv', skiprows=4)
print(data.head())
data_2020 = data[['Country Name', '2020']]
data_2020.columns = ['Country', 'Population']
data_2020.dropna(inplace=True)
data_2020 = data_2020.sort_values(by='Population', ascending=False).head(10)
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))
sns.barplot(x='Country', y='Population', data=data_2020, palette='viridis')
plt.title('Population Distribution by Country in 2020 (Top 10)', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
