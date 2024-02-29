import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
CPI 12- is the Inflation rate (calculated using the CPI index) calculated over a 12 month period.

Code generates a graph that allows you to compare the effect of inflation on gold price.

TO DO:
- Could improve graph by having the ticks on both y-axes match.
- Calculate local gradient of Gold price and see how it matches inflation. 
  Does gold price increase match inflation rate?
'''

df_inflation_orig = pd.read_csv('Inflation_Rate.csv')
df_gold_orig = pd.read_csv('Price_of_Gold.csv')


# Pre-process the data
# Change the dates so that they conform to the same structure with datetime
df_inflation = df_inflation_orig.copy()
df_inflation['Date'] = pd.to_datetime(df_inflation['Date'], format='%b-%y')
# df_inflation['Date'] = df_inflation['Date'].dt.to_period('M')
df_inflation['Date'] = df_inflation['Date'].dt.strftime('%Y-%m')

df_gold = df_gold_orig.copy()
df_gold['Date'] = df_gold['Date'].str.replace(' 00:00', '')
df_gold['Date'] = pd.to_datetime(df_gold['Date'], format='%d/%m/%Y')  # If it doesn't work, try %b instead of %m
# df_gold['Date'] = df_gold['Date'].dt.to_period('M')
df_gold['Date'] = df_gold['Date'].dt.strftime('%Y-%m')
# Remove duplicates to avoid problems with graph
df_gold_minus_duplicates = df_gold.drop_duplicates('Date', keep='first')

# repeat = df_gold[df_gold.duplicated('Date', keep=False)]
# print(repeat)

merged_df = pd.merge(df_inflation, df_gold_minus_duplicates, on='Date', how='inner')


print(df_inflation.head())
print(df_gold.head())
print(merged_df.head())

dates = merged_df['Date']
y_inflation = merged_df['CPI 12-']
y_gold      = merged_df['Close (kg)']

# print(x_inflation)


fig, ax1 = plt.subplots()

color1 = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('CPI 12', color=color1)
ax1.plot(dates, y_inflation, color=color1, label='inflation')
chosen_xticks = [i for i in range(len(dates)) if i % 6 == 0]  # [x for x, index in enumerate(x_inflation) if index % 2 == 0]
ax1.set_xticks(chosen_xticks)
ax1.set_xticklabels(dates.iloc[chosen_xticks], rotation=45)
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color2 = 'tab:blue'
ax2.set_ylabel('Gold Price (GBP/kg)', color=color2)
ax2.plot(dates, y_gold, color=color2, label='gold')
ax2.tick_params(axis='y', labelcolor=color2)

# plt.plot(dates, y_inflation)
# plt.plot(dates, y_gold)

ax1.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

fig.tight_layout()
plt.show()

'''
x_gold = 
y_gold = 
'''


# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [x**2 for x in numbers]
# print(squared_numbers)
