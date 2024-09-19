from tkinter.font import names

import pandas as pd

one = pd.read_excel('source/one.xlsx',sheet_name='testspreadsheet',header=0,engine='openpyxl')
two = pd.read_excel('source/two.xlsx',sheet_name='testspreadsheet',header=0,engine='openpyxl')
three = pd.read_excel('source/three.xlsx',sheet_name='testspreadsheet',header=0,engine='openpyxl')
four = pd.read_excel('source/four.xlsx',sheet_name='testspreadsheet',header=0,engine='openpyxl')
five = pd.read_excel('source/five.xlsx',sheet_name='testspreadsheet',header=0,engine='openpyxl')
six = pd.read_excel('source/six.xlsx',sheet_name='testspreadsheet',header=0,engine='openpyxl')

two['new'] = 'ok par'

df = pd.concat([one,two,three])

df = df[['name','job','id']]

print(pd.read_excel('source/five.xlsx' ,names= ['hello','kitty'] , usecols=[2,0] ))
print(two)
print(df)

