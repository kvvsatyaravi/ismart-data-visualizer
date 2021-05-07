
"""csv_file_path = askopenfilename()
file =(csv_file_path)
df=pd.read_excel(file)
first= StringVar()
E1 = Entry(window,textvariable = first,width=10)
E1.place(x = 120,y = 100)
l3 = Label(window,  text='from', width=15 )
l3.place(x=130,y=125)
second= StringVar()
E2 = Entry(window,textvariable= second,width=10)
E2.place(x = 220,y = 100)
l4 = Label(window,  text='to', width=15 )
l4.place(x=215,y=125)
def create_excel():
    firstval=first.get()
    secondval=second.get()
    for i in range(firstval,secondval):
        mask =  df['Order Quantity'].values <= i 
        df_new = df.loc[mask]
        print(df_new)
        df_new.to_excel('./test.xlsx')

"""




from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pandas as pd

def create_excel():
    firstval = int(E1.get())
    secondval = int(E2.get())
    for i in range(firstval,secondval):
        mask =  df['Sales'].values <= i 
        df_new = df.loc[mask]
        print(df_new)
        
        df_new.to_excel("./test1.xlsx")
        

window=Tk()
window.title("testing")
window.geometry("450x350")

csv_file_path = askopenfilename()
file =(csv_file_path)
df=pd.read_excel(file)
 

E1 = Entry(window,width=10)
E1.place(x = 120,y = 100)
l3 = Label(window,  text='from', width=15 )
l3.place(x=130,y=125)

E2 = Entry(window,width=10)
E2.place(x= 220,y= 100)
l4 = Label(window,  text='upto', width=15 )
l4.place(x=215,y=125)
but1=Button(window, text="button1",command=create_excel)
but1.place(x=175, y=150)
window.mainloop()
















