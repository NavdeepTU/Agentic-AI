# filename: stock_price_plot_yfinance.py

import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical stock price data for META (Facebook) and Tesla using yfinance
meta_data = yf.Ticker('META').history(period='max')
tesla_data = yf.Ticker('TSLA').history(period='max')

# Plot the stock price changes
plt.figure(figsize=(14, 7))
plt.plot(meta_data['Close'], label='META (Facebook) Stock Price', color='blue')
plt.plot(tesla_data['Close'], label='Tesla Stock Price', color='red')
plt.title('Historical Stock Price Comparison: META vs Tesla')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()