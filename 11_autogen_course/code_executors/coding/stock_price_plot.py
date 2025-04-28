# filename: stock_price_plot.py

import pandas as pd
import matplotlib.pyplot as plt

# Load the historical stock price data for META (Facebook) and Tesla
meta_stock_data = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/META?period1=0&period2=9999999999&interval=1d&events=history')
tesla_stock_data = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=0&period2=9999999999&interval=1d&events=history')

# Set the Date as the index for both dataframes
meta_stock_data.set_index('Date', inplace=True)
tesla_stock_data.set_index('Date', inplace=True)

# Plot the stock price changes
plt.figure(figsize=(14, 7))
plt.plot(meta_stock_data['Close'], label='META (Facebook) Stock Price', color='blue')
plt.plot(tesla_stock_data['Close'], label='Tesla Stock Price', color='red')
plt.title('Historical Stock Price Comparison: META vs Tesla')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()