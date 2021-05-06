import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

csv_file_path = askopenfilename()

file =(csv_file_path)
df=pd.read_excel(file)
first=int(input())
second=int(input())
for i in range(first,second):
    mask =  df['Order Quantity'].values <= i 
    df_new = df.loc[mask]
    print(df_new)
    df_new.to_excel('./test.xlsx')
