# author:Liu Yu
# time:2024/10/14 20:18
import pandas as pd
import baostock as bs
from datetime import datetime, timedelta

class A_Stocks_DataCollection:
    def __init__(self, start_date, end_date, current_date,stocks_num=10000):
        self.start_date = start_date
        self.end_date = end_date
        self.current_date = current_date
        self.stocks_num = stocks_num

    def get_data(self):
        result = self.get_stocks_code_name()
        result = self.get_stock_code_industry(result)
        self.get_history_k_data(result)

    def get_stocks_code_name(self):
        #### 登陆系统 ####
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)

        #### 获取证券信息 ####
        rs = bs.query_all_stock(day=self.previous_date())
        print('query_all_stock respond error_code:' + rs.error_code)
        print('query_all_stock respond  error_msg:' + rs.error_msg)

        #### 打印结果集 ####
        data_list = []
        while (rs.error_code == '0') and rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        return result

    def get_stock_code_industry(self, result):
        # 登陆系统
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)

        # 获取行业分类数据
        rs = bs.query_stock_industry()
        print('query_stock_industry error_code:' + rs.error_code)
        print('query_stock_industry respond  error_msg:' + rs.error_msg)

        # 打印结果集
        industry_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            industry_list.append(rs.get_row_data())
        industry_result = pd.DataFrame(industry_list, columns=rs.fields)

        # 假设 'code' 是两个 DataFrame 共有的列，用来做连接
        result = pd.merge(result, industry_result[['code', 'industry', 'industryClassification']], on='code', how='left')

        # 登出系统
        bs.logout()

        return result

    def get_history_k_data(self, result):
        # 登陆系统
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)

        #### 获取历史K线数据 ####
        for code in result["code"]:
            rs = bs.query_history_k_data_plus(code=code,
                                              fields="date,code,open,high,low,close,preclose,volume,"
                                                     "amount,adjustflag,turn,tradestatus,pctChg,peTTM,"
                                                     "pbMRQ,psTTM,pcfNcfTTM,isST",
                                              start_date=self.start_date,
                                              end_date=self.end_date,
                                              frequency="d",
                                              adjustflag="3")  # frequency="d"取日k线，adjustflag="3"默认不复权
            k_data_list = []
            while (rs.error_code == '0') and rs.next():
                # 获取一条记录，将记录合并在一起
                k_data_list.append(rs.get_row_data())
            k_result = pd.DataFrame(k_data_list, columns=rs.fields)
            k_result = pd.merge(k_result, result[['code', 'code_name','industry', 'industryClassification']], on='code',
                              how='left')
            k_result.to_csv(f"../data/A_Stocks_Data/{k_result['code'][0]}.csv",encoding="UTF-8", index=False)

        print('query_history_k_data_plus respond error_code:' + rs.error_code)
        print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)
        #### 登出系统 ####
        bs.logout()

    def previous_date(self):
        date_format = '%Y-%m-%d'
        date_obj = datetime.strptime(self.current_date, date_format)
        previous_date = date_obj - timedelta(days=1)
        previous_date_str = previous_date.strftime(date_format)
        return previous_date_str

