#!/anaconda3/bin/python

import xlrd
import sys



def head(file_):
    """
        basic command line script for writing an excel file
    """
    workbook = xlrd.open_workbook(file_)
    worksheet = workbook.sheet_by_index(0)
    num_cols = worksheet.ncols
    num_rows = worksheet.nrows
    str_ = ""
    for row in range(0,num_rows):
        for col in range(0,num_cols):
            cell = worksheet.cell(row,col).value
            print(str_ + "\t|\t"  + str(cell),end="")
        print("\t|\n",end="")

    
if __name__ == "__main__":
    head(sys.argv[1])
