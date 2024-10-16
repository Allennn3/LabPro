# author:Liu Yu
# time:2024/10/16 18:19
# 将最大列数设置为None，这样可以显示所有列
import yfinance as yf
import pandas as pd
import numpy as numpy
import datetime
from Get_American_Stocks_Tickers import get_XNYS_stock_tickers, get_XNAS_stock_tickers
from Tickers_to_csv import load_XNYS_json_to_csv, load_XNAS_json_to_csv

class American_Stocks_DataCollection:

    def get_data(self):
        self.get_XNYS_Data()
        self.get_XNAS_Data()

    def get_XNYS_Data(self):
        get_XNYS_stock_tickers()
        load_XNYS_json_to_csv()
        data = pd.read_csv("XNYS.csv")
        data = data.drop(data[data['is_active'] == 0].index, inplace=True)

        for stock_code in data['ticker'][:2]:
            tk = yf.Ticker(stock_code)

            tk_data = yf.download(stock_code, period="max")

            tk_data.reset_index(inplace=True)
            tk_data.insert(0, 'ticker', stock_code)

            tk_data = pd.merge(tk_data, data, on='ticker', how='left')

            tk_data['Sector'] = tk.info.get('sectorKey')
            tk_data['Industry'] = tk.info.get('industryKey')

            tk_data.to_csv(f"../data/American_Stocks_Data/{stock_code}.csv", index=False)

    def get_XNAS_Data(self):
        get_XNYS_stock_tickers()
        load_XNYS_json_to_csv()
        data = pd.read_csv("XNAS.csv")
        data = data.drop(data[data['is_active'] == 0].index, inplace=True)

        for stock_code in data['ticker'][:2]:
            tk = yf.Ticker(stock_code)

            tk_data = yf.download(stock_code, period="max")

            tk_data.reset_index(inplace=True)
            tk_data.insert(0, 'ticker', stock_code)

            tk_data = pd.merge(tk_data, data, on='ticker', how='left')

            tk_data['Sector'] = tk.info.get('sectorKey')
            tk_data['Industry'] = tk.info.get('industryKey')

            tk_data.to_csv(f"../data/American_Stocks_Data/{stock_code}.csv", index=False)