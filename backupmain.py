from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("ismart data filter")
        self.minsize(330,280)
        self.wm_iconbitmap('icon.ico')
        
        

# Function for opening the  
# file explorer window 
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("csv files", 
                                                        "*.csv*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    label_file_explorer.configure(text="File Opened: "+filename) 
       

gui = Tk(className='equalizer')
# set window size
gui.geometry("330x280")
gui.iconbitmap(r'C:\Documents and Settings\Administrator\Desktop\equalizer frontend\icon.ico')
style = Style()
style.configure('y.TButton', font = 
               ('calibri', 15, 'bold'), 
                    borderwidth = '4',foreground='red') 
style.configure('w.TButton', font = 
               ('calibri', 11, 'bold'), 
                foreground = 'black') 
w = Canvas(gui)
w.pack()

w.create_line(200,30, 200, 260, fill="black", width=1)

buttonExample1 = Button(gui,
                           text="select file",
                        style='y.TButton',
                        command=browseFiles)
buttonExample1.place(x=20, y=100)

buttonExample2 = Button(gui,
                           text="output",
                           style= 'w.TButton')
buttonExample2.place(x=225,y=50)

buttonExample3 = Button(gui,
                           text="filter",
                           style="w.TButton")
buttonExample3.place(x=225,y=190)


gui.mainloop()
