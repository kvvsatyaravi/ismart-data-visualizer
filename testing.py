import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

csv_file_path = askopenfilename()

file =(csv_file_path)
df=pd.read_excel(file)

mask =  df['Order Quantity'].values <= 2 

df_new = df.loc[mask]
print(df_new)
df_new.to_excel('./test.xlsx')
