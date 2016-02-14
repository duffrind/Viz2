plt.figure(num=1,figsize=(2.25,1.5))
y = sp500['Close']
x = sp500['Date']
volatility_multiple = np.sqrt(252) #252 trading days in a year
new_x = (x - pd.to_datetime('2010-01-29')).astype('timedelta64[D]')
market_m,market_b = polyfit(new_x, y,1) 
market_sd = np.std(y.iloc[-10:]) # Last 10 days
plt.plot(x,y,label='_nolabel_')
plt.plot(x,market_m*new_x+market_b,'r',label='Regression Line')
plt.title('S&P 500')
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
total_days = new_x[0]
market_apy = ((y.iloc[0]/y.iloc[-1])**(365/total_days)-1)
print('Market APY:', "%.1f" % (market_apy * 100), '%')
average_market_apy = (((market_m*total_days+market_b)/(market_b))**(365/total_days)-1)
print('Average Market APY:', "%.1f" % (average_market_apy*100),'%')
scaled_market_m = market_m/y.iloc[-1]
scaled_market_b = market_b/y.iloc[-1]
print('Projected Market Volatility (Next 10 Days):', "%.1f" % (market_sd*volatility_multiple),'%')
market_profit = (5000*y.iloc[0]/y.iloc[-1])-5000
print('Nominal Market Profit: $', "%.2f" % market_profit) # Assuming no trading costs
#There has been about 10.5% inflation since early 2010
inflation_rate = 1.105
real_market_profit = market_profit/inflation_rate
print('Real Market Profit: $', "%.2f" % real_market_profit)