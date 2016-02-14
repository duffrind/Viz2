plt.figure(num=1,figsize=(2.25,1.5))
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