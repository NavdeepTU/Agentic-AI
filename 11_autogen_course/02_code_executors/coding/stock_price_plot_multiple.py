# filename: stock_price_plot_multiple.py

import yfinance as yf
import matplotlib.pyplot as plt

# Define a list of stock symbols
stocks = ['META', 'TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL']

plt.figure(figsize=(14, 7))

# Fetch historical stock price data for each stock symbol and plot their closing prices
for stock in stocks:
    data = yf.Ticker(stock).history(period='1y')
    plt.plot(data['Close'], label=f'{stock} Stock Price')

plt.title('Historical Stock Price Comparison: META vs Tesla vs Google vs Amazon vs Microsoft vs Apple (1 year)')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()