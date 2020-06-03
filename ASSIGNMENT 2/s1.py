import pandas as pd
#accessing excel sheets
files = pd.ExcelFile('assign.xlsx')
print('Files are accessed and reading is completed using pandas')
#converting file .xlsx into .csv file format
for i in range(10):
    s=files.parse('sheet'+str(i+1))
    s.to_csv('csvfile'+str(i+1),sep=',')
print('files of .xlsx is converted into .csv files')



