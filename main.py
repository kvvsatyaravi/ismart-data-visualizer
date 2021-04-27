from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pandas as pds

#developer:ravi
#demo version
#packages for excel (xlrd,openpyxl)
#class Root is main core that connects to all backend logics

class Root(Tk):

    #__init__ constructor
    def __init__(self):
        super(Root, self).__init__()
        self.title("ismart data filter")
        self.wm_iconbitmap('icon.ico')
        self.geometry("330x280") 
        w = Canvas()
        w.pack()
        w.create_line(200,30, 200, 260, fill="black", width=1)
        style = Style()
        style.configure('y.TButton', font = ('calibri', 15, 'bold'), borderwidth = '4',foreground='red') 
        style.configure('w.TButton', font = ('calibri', 11, 'bold'), foreground = 'black')
        self.main()
        

    def import_csv_data(self):
        csv_file_path = askopenfilename()
        print(csv_file_path)
        file =(csv_file_path)
        newData = pds.read_excel(file)
        pd_xl_file=pds.ExcelFile(file)
        parsing =pd_xl_file.parse("Sheet1")
        col_count=len(parsing.axes[1])
        print("no of collumns is",col_count)
        row=newData.head(0)
        datacol = newData.columns
        if file.find('.xlsx')==0:
            print("please upload excel file")
        else:
            print("selected file is under process")
            window = Tk()
            window.wm_iconbitmap('icon.ico')
            window.title("filtering process")
            window.geometry('350x200')

            # Option menu variable
            
            for i in range(col_count):
                list_col=list()
                col=newData.columns[i]
                print(col)
                list_col=list_col.append(col)
            print(list_col)    
            print(columns)
            optionVar = StringVar()
            option = OptionMenu(window, optionVar, "dummy",columns)
            option.pack()

                    # Create button with command
            def show():
                print("Selected value :", optionVar.get())

                btnShow = Button(window, text="Show", command=show)
                btnShow.pack()
                window.mainloop()

                    # Create button with command
            def show():
                print("Selected value :", optionVar.get())

                btnShow = Button(window, text="Show", command=show)
                btnShow.pack()

            
    #df = pd.read_csv(csv_file_path)
    
    #insert csv or excel file button
    def main(self):
        buttonExample1 = Button(text="select file",
                                style='y.TButton',command=self.import_csv_data)
        buttonExample1.place(x=20, y=100)
        

        buttonExample2 = Button(text="filter",
                                   style= 'w.TButton',command=self.filter)
        buttonExample2.place(x=225,y=50)

        buttonExample3 = Button(text="output",
                                   style="w.TButton")
        buttonExample3.place(x=225,y=190)
        

    #data filter considered as o/p
    
    def filter(self):
        data=self.import_csv_data()
        if data.find('.xlsx')==0:
            print("please upload excel file")
            
        else:
            print("selected file is under process")
            

        #data filter considered as o/p
    def output(self):
        print("uncompleted module")
        
root =Root()

root.mainloop()
