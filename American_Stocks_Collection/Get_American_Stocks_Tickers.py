# author:Liu Yu
# time:2024/10/15 22:12
import requests
import json

def get_stock_tickers(i):
    if i=="XNYS":
        #'exchange_code': 'XNYS', 'exchange_name': '纽约证券交易所'
        url = f"https://tsanghi.com/api/fin/stock/XNYS/list?token=d33203b83c9348a2abd529e85856c30e"
    elif i=="XNAS":
        #'exchange_code': 'XNAS', 'exchange_name': '纳斯达克证券交易所'
        url = f"https://tsanghi.com/api/fin/stock/XNAS/list?token=d33203b83c9348a2abd529e85856c30e"

    response = requests.get(url)

    # 检查响应状态
    if response.status_code == 200:
        data = response.json()
        # 将 JSON 数据保存到文件中
        with open(i+'.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print("数据已保存到 "+i+".json 文件中。")
    else:
        print(f"请求失败，状态码: {response.status_code}")



# def get_XNAS_stock_tickers():
#     #'exchange_code': 'XNAS', 'exchange_name': '纳斯达克证券交易所'
#     url = f"https://tsanghi.com/api/fin/stock/XNAS/list?token=d33203b83c9348a2abd529e85856c30e"

#     response = requests.get(url)


#     # 检查响应状态
#     if response.status_code == 200:
#         data = response.json()
#         # 将 JSON 数据保存到文件中
#         with open('XNAS.json', 'w', encoding='utf-8') as file:
#             json.dump(data, file, ensure_ascii=False, indent=4)
#             print("数据已保存到 XNAS.json 文件中。")
#     else:
#         print(f"请求失败，状态码: {response.status_code}")