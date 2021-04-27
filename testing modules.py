import pandas as pd
#selected specfic row of column
path=("C:/Users/yevad/Desktop/Book1.xlsx")
df = pd.read_excel(path)
df.head()
loca=df.loc[df['flatno'] == 'b1']
print(loca)
