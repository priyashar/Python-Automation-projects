import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
excel_file1 = 'shift-data.xlsx'
excel_file2 = 'third-shift-data.xlsx'
df1= pd.read_excel(excel_file1,sheet_name='first')
df2= pd.read_excel(excel_file1,sheet_name='second')
df3=pd.read_excel(excel_file2)
df_all= pd.concat([df1,df2,df3])
# print(df_all)
pivot=df_all.groupby(['Shift']).mean()
shift_prod=pivot.loc[:,"Production Run Time (Min)":"Products Produced (Units)"]
# print(shift_prod)
# shift_prod.plot(kind='bar')
# plt.show()
df_all.to_excel("output.xlsx")