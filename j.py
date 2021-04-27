import pandas as pd
pd_xl_file = pd.ExcelFile("C:/Users/yevad/Desktop/Book1.xlsx")
df = pd_xl_file.parse("Sheet1")

total_cols=len(df.axes[1])
print(total_cols)
