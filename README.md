# Lab_Pro

## requirements
*pandas<br>
*baostock<br>
*yfinance<br>

## Project Structure
### Run the code

Run the following command to run POCL
```
python main.py

### A_Stocks_Collection
*'''A_Stocks_DataCollection.py''': is uesd to download and collect all A_stocks data
*'''testAll.py''': is only a test file to test the completeness and accuracy of the whole process

### American_Stocks_Collection
*'''A_Stocks_DataCollection.py''': is uesd to download and collect all American_stocks data
*'''testAll.py''': is only a test file to test the completeness and accuracy of the whole process
*'''Get_American_Stocks_Tickers.py''': used to acquire all the tickers of American stocks including 'XNAS' and 'XNYS'.
                                    Because there is only a interface that you must input the ticker to obtain the stocks historic information
*'''Tickers_to_csv.py''':After above process, you will get a json file.And this script is used to format json to csv and concatenate all the uesful features.

### data
*It's uesd to store the stocks data file.
