# 将最大列数设置为None，这样可以显示所有列
import yfinance as yf
import pandas as pd
import numpy as numpy
from datetime import datetime, timedelta
from American_Stocks_Collection.Get_American_Stocks_Tickers import get_stock_tickers
from American_Stocks_Collection.Tickers_to_csv import load_json_to_csv

class American_Stocks_DataCollection:
    def __init__(self, start_date, end_date, current_date, stocks_num=10000):
        self.start_date = start_date
        self.end_date = end_date
        self.current_date = current_date
        self.stocks_num = stocks_num


    # def get_data(self):
    #     self.get_XNYS_Data(start_date,end_date)
    #     # self.get_XNAS_Data()

    def get_data(self,start_date,end_date):
        for i in ["XNYS","XNAS"]:
            get_stock_tickers(i)
            load_json_to_csv(i)
            data = pd.read_csv(i+".csv")
            # data = data[data['is_active'] != 0]

            for stock_code in data['ticker'][:2]:
                tk = yf.Ticker(stock_code)

                tk_data = yf.download(stock_code, start=start_date, end=end_date, period="max")

                tk_data.reset_index(inplace=True)
                tk_data.insert(0, 'ticker', stock_code)

                tk_data = pd.merge(tk_data, data, on='ticker', how='left')

                tk_data['Sector'] = tk.info.get('sectorKey')
                tk_data['Industry'] = tk.info.get('industryKey')

                start_date_1 = datetime.strptime(start_date, '%Y-%m-%d')
                end_date_1 = datetime.strptime(end_date, '%Y-%m-%d')

                if end_date_1-timedelta(days=1)==start_date_1:
                    tk_data.to_csv(f"data/American_Stocks_Data/{stock_code}.csv", index=False, mode="a", header=0)
                else:
                    tk_data.to_csv(f"data/American_Stocks_Data/{stock_code}.csv", index=False)



    # def get_XNYS_Data(self,start_date,end_date):
    #     get_XNYS_stock_tickers()
    #     load_XNYS_json_to_csv()
    #     data = pd.read_csv("XNYS.csv")
    #     data = data.drop(data[data['is_active'] == 0].index, inplace=True)

    #     for stock_code in data['ticker'][:2]:
    #         tk = yf.Ticker(stock_code)

    #         tk_data = yf.download(stock_code, start=start_date, end=end_date, period="max")

    #         tk_data.reset_index(inplace=True)
    #         tk_data.insert(0, 'ticker', stock_code)

    #         tk_data = pd.merge(tk_data, data, on='ticker', how='left')

    #         tk_data['Sector'] = tk.info.get('sectorKey')
    #         tk_data['Industry'] = tk.info.get('industryKey')

    #         tk_data.to_csv(f"data/American_Stocks_Data/{stock_code}.csv", index=False)

    # def get_XNAS_Data(self):
    #     get_XNYS_stock_tickers()
    #     load_XNYS_json_to_csv()
    #     data = pd.read_csv("XNAS.csv")
    #     data = data.drop(data[data['is_active'] == 0].index, inplace=True)

    #     for stock_code in data['ticker'][:2]:
    #         tk = yf.Ticker(stock_code)

    #         tk_data = yf.download(stock_code, period="max")

    #         tk_data.reset_index(inplace=True)
    #         tk_data.insert(0, 'ticker', stock_code)

    #         tk_data = pd.merge(tk_data, data, on='ticker', how='left')

    #         tk_data['Sector'] = tk.info.get('sectorKey')
    #         tk_data['Industry'] = tk.info.get('industryKey')

    #         tk_data.to_csv(f"../data/American_Stocks_Data/{stock_code}.csv", index=False)