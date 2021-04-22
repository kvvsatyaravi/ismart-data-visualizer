from tkinter import * 
from tkinter.ttk import *
  
# importing askopenfile function 
# from class filedialog 
from tkinter import filedialog
  



def browsefile(): 
    file_path = filedialog.askopenfilename()
    return file_path

