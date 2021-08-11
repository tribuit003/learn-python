import openpyxl

filename = 'file.xlsx'
cellname = 'A1'

def get_value_excel(filename, cellname):
    wb = openpyxl.load_workbook(filename)
    Sheet1 = wb['Sheet1']
    wb.close()
    return Sheet1[cellname].value

print(get_value_excel(filename, cellname))