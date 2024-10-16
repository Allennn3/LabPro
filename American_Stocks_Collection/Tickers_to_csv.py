# author:Liu Yu
# time:2024/10/15 22:59
# 将JSON数据加载为Python字典
import json
import csv



def load_XNYS_json_to_csv(json_file, csv_file):
    # XNYS_toCSV
    # 打开并读取 JSON 文件
    with open('XNYS.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 打开一个新的CSV文件用于写入
    with open('XNYS.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # 创建一个csv.DictWriter对象，指定字段名
        fieldnames = ['ticker', 'name', 'is_active', 'exchange_code', 'country_code', 'currency_code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 写入表头
        writer.writeheader()

        # 遍历data中的每个条目并写入CSV文件
        for item in data['data']:
            writer.writerow(item)

    print("XNYS.csv文件已生成")
    
def load_XNAS_json_to_csv(json_file, csv_file):
    #XNAS_toCSV
    # 打开并读取 JSON 文件
    with open('XNAS.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 打开一个新的CSV文件用于写入
    with open('XNAS.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # 创建一个csv.DictWriter对象，指定字段名
        fieldnames = ['ticker', 'name', 'is_active', 'exchange_code', 'country_code', 'currency_code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 写入表头
        writer.writeheader()

        # 遍历data中的每个条目并写入CSV文件
        for item in data['data']:
            writer.writerow(item)

    print("XNAS.csv文件已生成")