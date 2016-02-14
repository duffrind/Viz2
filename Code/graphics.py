#S&P 500
plt.figure(num=1,figsize=(4.5,3))
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

#Apple
plt.figure(num=1,figsize=(4.5,3))
y = apple['Close']
x = apple['Date']
m,b = polyfit(new_x, y, 1) 
sd = np.std(y.iloc[-10:]) # Last 10 days
apple_scaled_m = scaled_market_m * y.iloc[-1]
apple_scaled_b = scaled_market_b * y.iloc[-1]
plt.plot(x,y,label='_nolegend_')
plt.plot(x,m*new_x+b,label='Regression Line')
x1,x2,y1,y2 = plt.axis()
plt.plot(x,apple_scaled_m*new_x+apple_scaled_b,label='Scaled Market Average')
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.title('Apple')
plt.axis((x1,x2,y1,y2))
plt.legend()
plt.show()
apy = ((y.iloc[0]/y.iloc[-1])**(365/total_days)-1)
print('Absolute APY: ', "%.1f" % (apy * 100), '%')
ave_apy = (((m*total_days+b)/(b))**(365/total_days)-1)
print('Absolute Average APY:',"%.1f" % (ave_apy*100),'%')
print('Relative APY: ', "%.1f" % ((apy-market_apy)*100),'%')
print('Relative Average APY:', "%.1f" % ((ave_apy-average_market_apy)*100),'%')
print('Projected Volatility (Next 10 Days):', "%.1f" % (sd*volatility_multiple),'%')
print('Percentage of Market Volatility:', "%.1f" % (sd/market_sd*100),'%')
profit = (5000*y.iloc[0]/y.iloc[-1])-5000+ sum(applediv['Dividends'])
print('Nominal Market Profit: $', "%.2f" % profit) # Assuming no trading costs
#There has been about 10.5% inflation since early 2010
real_profit = profit/inflation_rate
print('Real Market Profit: $', "%.2f" % real_profit)

#Bank of America
plt.figure(num=1,figsize=(4.5,3))
y = boa['Close']
x = boa['Date']
m,b = polyfit(new_x, y, 1) 
sd = np.std(y.iloc[-10:]) # Last 10 days
boa_scaled_m = scaled_market_m * y.iloc[-1]
boa_scaled_b = scaled_market_b * y.iloc[-1]
plt.plot(x,y,label='_nolegend_')
plt.plot(x,m*new_x+b,label='Regression Line')
x1,x2,y1,y2 = plt.axis()
plt.plot(x,boa_scaled_m*new_x+boa_scaled_b,label='Scaled Market Average')
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.title('BoA')
plt.axis((x1,x2,y1,y2))
plt.legend()
plt.show()
apy = ((y.iloc[0]/y.iloc[-1])**(365/total_days)-1)
print('Absolute APY:', "%.1f" % (apy * 100), '%')
ave_apy = (((m*total_days+b)/(b))**(365/total_days)-1)
print('Absolute Average APY:', "%.1f" % (ave_apy*100),'%')
print('Relative APY: ', "%.1f" % ((apy-market_apy)*100),'%')
print('Relative Average APY:', "%.1f" % ((ave_apy-average_market_apy)*100),'%')
print('Projected Volatility (Next 10 Days):', "%.1f" % (sd*volatility_multiple),'%')
print('Percentage of Market Volatility:', "%.1f" % (sd/market_sd*100),'%')
profit = (5000*y.iloc[0]/y.iloc[-1])-5000+ sum(boadiv['Dividends'])
print('Nominal Market Profit: $', "%.2f" % profit) # Assuming no trading costs
#There has been about 10.5% inflation since early 2010
real_profit = profit/inflation_rate
print('Real Market Profit: $', "%.2f" % real_profit)

#GE
plt.figure(num=1,figsize=(4.5,3))
y = ge['Close']
x = ge['Date']
m,b = polyfit(new_x, y, 1) 
sd = np.std(y.iloc[-10:]) # Last 10 days
ge_scaled_m = scaled_market_m * y.iloc[-1]
ge_scaled_b = scaled_market_b * y.iloc[-1]
plt.plot(x,y,label='_nolegend_')
plt.plot(x,m*new_x+b,label='Regression Line')
x1,x2,y1,y2 = plt.axis()
plt.plot(x,ge_scaled_m*new_x+ge_scaled_b,label='Scaled Market Average')
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.title('GE')
plt.axis((x1,x2,y1,y2))
plt.legend()
plt.show()
apy = ((y.iloc[0]/y.iloc[-1])**(365/total_days)-1)
print('Absolute APY:', "%.1f" % (apy * 100), '%')
ave_apy = (((m*total_days+b)/(b))**(365/total_days)-1)
print('Absolute Average APY:', "%.1f" % (ave_apy*100),'%')
print('Relative APY: ', "%.1f" % ((apy-market_apy)*100),'%')
print('Relative Average APY:', "%.1f" % ((ave_apy-average_market_apy)*100),'%')
print('Projected Volatility (Next 10 Days):', "%.1f" % (sd*volatility_multiple),'%')
print('Percentage of Market Volatility:', "%.1f" % (sd/market_sd*100),'%')
profit = (5000*y.iloc[0]/y.iloc[-1])-5000+ sum(gediv['Dividends'])
print('Nominal Market Profit: $', "%.2f" % profit) # Assuming no trading costs
#There has been about 10.5% inflation since early 2010
real_profit = profit/inflation_rate
print('Real Market Profit: $', "%.2f" % real_profit)

#Exxon
plt.figure(num=1,figsize=(4.5,3))
y = exxon['Close']
x = exxon['Date']
m,b = polyfit(new_x, y, 1) 
sd = np.std(y.iloc[-10:]) # Last 10 days
exxon_scaled_m = scaled_market_m * y.iloc[-1]
exxon_scaled_b = scaled_market_b * y.iloc[-1]
plt.plot(x,y,label='_nolegend_')
plt.plot(x,m*new_x+b,label='Regression Line')
x1,x2,y1,y2 = plt.axis()
plt.plot(x,exxon_scaled_m*new_x+exxon_scaled_b,label='Scaled Market Average')
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.title('Exxon')
plt.axis((x1,x2,y1,y2))
plt.legend()
plt.show()
apy = ((y.iloc[0]/y.iloc[-1])**(365/total_days)-1)
print('Absolute APY:', "%.1f" % (apy * 100), '%')
ave_apy = (((m*total_days+b)/(b))**(365/total_days)-1)
print('Absolute Average APY:', "%.1f" % (ave_apy*100),'%')
print('Relative APY: ', "%.1f" % ((apy-market_apy)*100),'%')
print('Relative Average APY:', "%.1f" % ((ave_apy-average_market_apy)*100),'%')
print('Projected Volatility (Next 10 Days):', "%.1f" % (sd*volatility_multiple),'%')
print('Percentage of Market Volatility:', "%.1f" % (sd/market_sd*100),'%')
profit = (5000*y.iloc[0]/y.iloc[-1])-5000+ sum(exxondiv['Dividends'])
print('Nominal Market Profit: $', "%.2f" % profit) # Assuming no trading costs
#There has been about 10.5% inflation since early 2010
real_profit = profit/inflation_rate
print('Real Market Profit: $', "%.2f" % real_profit)

#Walmart
plt.figure(num=1,figsize=(4.5,3))
y = walmart['Close']
x = walmart['Date']
m,b = polyfit(new_x, y, 1) 
sd = np.std(y.iloc[-10:]) # Last 10 days
walmart_scaled_m = scaled_market_m * y.iloc[-1]
walmart_scaled_b = scaled_market_b * y.iloc[-1]
plt.plot(x,y,label='_nolegend_')
plt.plot(x,m*new_x+b,label='Regression Line')
x1,x2,y1,y2 = plt.axis()
plt.plot(x,walmart_scaled_m*new_x+walmart_scaled_b,label='Scaled Market Average')
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.title('Walmart')
plt.axis((x1,x2,y1,y2))
plt.legend()
plt.show()
apy = ((y.iloc[0]/y.iloc[-1])**(365/total_days)-1)
print('Absolute APY:', "%.1f" % (apy * 100), '%')
ave_apy = (((m*total_days+b)/(b))**(365/total_days)-1)
print('Absolute Average APY:', "%.1f" % (ave_apy*100),'%')
print('Relative APY: ', "%.1f" % (apy-market_apy*100),'%')
print('Relative Average APY:', "%.1f" % ((ave_apy-average_market_apy)*100),'%')
print('Projected Volatility (Next 10 Days):', "%.1f" % (sd*volatility_multiple),'%')
print('Percentage of Market Volatility:', "%.1f" % (sd/market_sd*100),'%')
profit = (5000*y.iloc[0]/y.iloc[-1])-5000+ sum(walmartdiv['Dividends'])
print('Nominal Market Profit: $', "%.2f" % profit) # Assuming no trading costs
#There has been about 10.5% inflation since early 2010
real_profit = profit/inflation_rate
print('Real Market Profit: $', "%.2f" % real_profit)