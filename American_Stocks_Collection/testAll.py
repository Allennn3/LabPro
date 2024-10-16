# author:Liu Yu
# time:2024/10/16 18:33
import pandas as pd
import yfinance as yf
data = pd.read_csv("XNAS.csv")
data.drop(data[data['is_active'] == 0].index, inplace=True)

for stock_code in data['ticker'][:3]:
    tk = yf.Ticker(stock_code)

    tk_data = yf.download(stock_code, period="max")

    tk_data.reset_index(inplace=True)
    tk_data.insert(1, 'ticker', stock_code)

    tk_data = pd.merge(tk_data, data, on='ticker', how='left')

    tk_data['Sector'] = tk.info.get('sectorKey')
    tk_data['Industry'] = tk.info.get('industryKey')


    tk_data.to_csv(f"../data/American_Stocks_Data/{stock_code}.csv", index=False)

