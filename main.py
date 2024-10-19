# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from A_Stocks_Collection import A_Stocks_DataCollection
from American_Stocks_Collection import American_Stocks_DataCollection
import schedule
import time
import datetime
from datetime import datetime, timedelta


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Baostock包中，若在每日交易数据上传之前查询当日交易数据，会报错
    # 获取当前日期
    today = datetime.now()
    # 格式化日期为YYYY-MM-DD
    formatted_date = today.strftime('%Y-%m-%d')
    print(formatted_date)

    A_Stocks_Data = A_Stocks_DataCollection.A_Stocks_DataCollection('2024-01-01', '2024-10-16', '2024-10-16')
    # 获取历史数据（只需要获取一次）
    A_Stocks_Data.get_data()


    #yfinance包中，若在每日交易数据上传之前查询当日交易数据，查询不到当日数据，但不会报错。
    American_Stocks_Data = American_Stocks_DataCollection.American_Stocks_DataCollection('2024-01-01', '2024-10-16', formatted_date)
    # 获取历史数据（只需要获取一次）
    American_Stocks_Data.get_data('2024-01-01', '2024-10-16')

    def fetch_info():
        A_Stocks_Data.get_new_data()
        American_Stocks_Data.get_data(formatted_date, formatted_date + timedelta(days=1))


    # 每天晚上 23 点执行
    # schedule.every().day.at("23:00").do(fetch_info)

    while True:
        schedule.run_pending()
        time.sleep(1)



