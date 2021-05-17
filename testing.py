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

    #frontend buttons
    def main(self):
        buttonExample1 = Button(text="select file",
                                style='y.TButton',command=self.import_data)
        buttonExample1.place(x=20, y=100)
        
        buttonExample2 = Button(text="filter",
                                   style= 'w.TButton',command=self.filter)
        buttonExample2.place(x=225,y=50)

        buttonExample3 = Button(text="output",
                                   style="w.TButton",command=self.output)
        buttonExample3.place(x=225,y=190)
        

    #import_csv_Dat contains logics of filtering process
    def import_data(self):
        file_path = askopenfilename()
        print(file_path)
        file =(file_path)

        if file.find('.xlsx') == 1:
            xlsxfile()            
        elif file.find('.csv') == 1:
            csvfile()
        else:
            print("cannot find excel file and csv file")
            return 0

    def xlsxfile(self):
        newData = pds.read_excel(file)
        pd_xl_file = pds.ExcelFile(file)
        parsing = pd_xl_file.parse("Sheet1")
        col_count = len(parsing.axes[1])
        print("no of collumns is",col_count)
        row = newData.head(0)
        datacol = newData.columns
        print("selected file is under process")
        window = Tk()
        window.wm_iconbitmap('icon.ico')
        window.title("filtering process")
        window.geometry('350x200')

        # Option menu variable
        list_col=[]
        for i in range(col_count):
            col=newData.columns[i]
            print("entered column no",i,"column value is",col)
            list_col.insert(i,col)
            print(list_col)

        def coldata():
            specficcol=newData[[optionVar.get()]]
            print("Selected value :", optionVar.get())
            print("selected column values:", specficcol)


        def create_excel():
            firstval = int(E1.get())
            secondval = int(E2.get())
            optionval = optionVar.get()
            df_tech_select_columns = newData.loc[(newData[optionval] >= firstval) & (newData[optionval] <= secondval )]
            print(df_tech_select_columns)
            df_tech_select_columns.to_excel("./test.xlsx")

        l1 = Label(window,  text='Select Column:', width=15 )
        l1.place(x=45,y=25)
        optionVar = StringVar(root)
        optionVar.set("select option")
        option = OptionMenu(window, optionVar, *list_col)
        option.place(x=130,y=25)
        l2 = Label(window,  text='advanced filter :', width=15 )
        l2.place(x=24,y=100)
        selnum= StringVar(root)
        E1 = Entry(window,width=10)
        E1.place(x = 120,y = 100)
        l3 = Label(window,  text='from', width=15 )
        l3.place(x=130,y=125)
        E2 = Entry(window,width=10)
        E2.place(x = 200,y = 100)
        l4 = Label(window,  text='to', width=15 )
        l4.place(x=215,y=125)
        btnShow = Button(window, text="Column values", command=coldata)
        btnShow.place(x=130,y=50)    
        btnShow2 = Button(window, text="Submit",command=create_excel)
        btnShow2.place(x=130,y=150)
            
        window.mainloop()

    def csvfile(self):
        print("underprocess")
        


    #data filter considered as filtering data logic
    def filter(self):
        self.import_data()
            

    #output considered as showing filtered data
    def output(self):
                # Create Object
        print("under process")

root = Root()
root.mainloop()


