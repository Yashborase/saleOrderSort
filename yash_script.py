#Dependancies : Pandas , Openpyxl 
import pandas as pd
data = pd.read_excel('order_sell.xlsx')
output = pd.DataFrame(data.groupby(by = 'Order Date')['Sales'].sum()).sort_values(by='Order Date' , ascending= False).reset_index()
output.to_csv("output.csv" , index= False)

