from xlrd import open_workbook, XLRDError
import pandas as pd

class ExcelInput:
    def __init__(self,path,name,rowNumber_ColumnHeader):
        self.path = path
        self.name = name
        self.rowNumber_ColumnHeader = rowNumber_ColumnHeader

    # This would be the 1st call to validate if the File passed is a valid Excel or not
    # If the file is a valid Excel we call other validator functions
    def IsFileValidExcel(self):
        try:
            excelWorkBook = open_workbook(self.path + '/' + self.name)
            return 1

        except XLRDError as e:
            return 0

    def IsColumnPresentAtMentionedRow(self):
        try:
            Excel_DataFrame = pd.read_excel((self.path + '/' + self.name),header=self.rowNumber_ColumnHeader)
            # print(Excel_DataFrame.head(2))
            print(list(Excel_DataFrame.columns))
            column_list = list(Excel_DataFrame.columns)
            column_list = list(filter(lambda x: not(x.startswith('Unnamed:')),column_list ))
            print(column_list)
        except IndexError as e:
            print('The Index is not valid')



ExcelObject = ExcelInput('C:/git/project-X/Data','SampleExcelFile.xlsx',1)
print(ExcelObject.IsFileValidExcel())
print(ExcelObject.IsColumnPresentAtMentionedRow())
