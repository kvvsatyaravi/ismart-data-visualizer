from tkinter.filedialog import askopenfilename
      
file_path = askopenfilename()

"""
if file_path.find('.xlsx'):
    print("input file is excel")           

elif file_path.find('.csv'):
    print("input file is csv")

else:
    print("cannot find excel file and csv file")"""

print(file_path)
print(file_path.endswith('.xlsx'))
