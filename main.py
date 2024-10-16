# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from A_Stocks_Collection import A_Stocks_DataCollection
from American_Stocks_Collection import American_Stocks_DataCollection



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Baostock包中，若在每日交易数据上传之前查询当日交易数据，会报错
    A_Stocks_Data = A_Stocks_DataCollection('2000-01-01', '2023-01-06', '2024-10-15')
    A_Stocks_Data.get_data()
    #yfinance包中，若在每日交易数据上传之前查询当日交易数据，查询不到当日数据，但不会报错。
    American_Stocks_Data = American_Stocks_DataCollection()
    American_Stocks_Data.get_data()

