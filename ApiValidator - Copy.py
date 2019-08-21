import csv 

##csv 
class csvInput:
    def __init__(self,path,name,rowNumber_ColumnHeader,fileDelimiter):
        self.path = path
        self.name = name
        self.rowNumber_ColumnHeader = rowNumber_ColumnHeader
        self.fileDelimiter = fileDelimiter

    # This would be the 1st call to validate if the File passed is a valid csv or not
    # If the file is a valid Excel we call other validator functions
    def IsFileValidCSV(self):
        try:
             
            with open(self.path + self.name,'r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter = self.fileDelimiter)
                csvfile.close()
            return 1

        except csv.Error as e:
            return 0

    def IsColumnPresentAtMentionedRow(self):
        try:
            with open(self.path + self.name,'r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter= self.fileDelimiter)
                rows = list(csv_reader)
                csvfile.close()
            return rows[self.rowNumber_ColumnHeader]

        except IndexError as e:
            print('The Index is not valid')



csvObject = csvInput('c:\\Users\\salman\\Desktop\\ProjectX\\','InputCSV1.csv',0,'\t')
print(csvObject.IsFileValidCSV())
print(csvObject.IsColumnPresentAtMentionedRow())
 