import openpyxl
#wb=openpyxl.load_workbook(r'C:\Users\SagnikBhattacharya\Desktop\files\nestedfolder\store.xlsx')
wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']='Year'
sheet['B1']='Sales'
d={2017:150000,2018:180000,2019:210000,2020:125000}
for i in d.items():
    sheet.append(i)
wb.save(r'C:\Users\SagnikBhattacharya\Desktop\files\nestedfolder\yr.xlsx')