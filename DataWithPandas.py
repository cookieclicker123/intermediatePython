import pandas as pd

filePath = '/Users/seb/Documents/archive/Finance_data.csv'

# Read the data 
data = pd.read_csv(filePath)

# Replace 0 with NA in 'Equity_Market' column
data['Equity_Market'].replace(0, pd.NA, inplace=True)

# Calculate descriptive statistics for 'Mutual_Funds' and 'Equity_Market'
desc_mutual_funds = data['Mutual_Funds'].describe()
desc_equity_market = data['Equity_Market'].describe()

# Divide the statistics of 'Mutual_Funds' by the corresponding statistics of 'Equity_Market'
ratio_stats = desc_mutual_funds / desc_equity_market

# Get descriptive statistics for the DataFrame
desc_data = data.describe()

# Add 'fundsToStocks' column to the descriptive statistics DataFrame
# Using reindex to align the index of ratio_stats with desc_data
desc_data['fundsToStocks'] = ratio_stats.reindex(desc_data.index)

# Set display precision
pd.set_option('display.precision', 10)

# Display the first few rows of 'Mutual_Funds', 'Equity_Market'
print(data[['Mutual_Funds', 'Equity_Market']].head())

# Display the modified descriptive statistics
print(desc_data)
print()

# Other outputs
print(data.dtypes)
print()
print(data.info()) 
print()
print(data.isnull().sum())
print()
print("-------------------")

import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(desc_data['fundsToStocks'])
plt.title('Distribution of Funds to Stocks Ratio')
plt.xlabel('Funds to Stocks Ratio Value')
plt.ylabel('Frequency')
plt.show()