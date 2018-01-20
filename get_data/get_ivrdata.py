#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Qiaoxueyuan
@time: 2017/8/1 14:25
'''
import xlrd


class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        # get titles
        self.row = self.table.row_values(0)

        # get rows number
        self.rowNum = self.table.nrows

        # get columns number
        self.colNum = self.table.ncols

        # the current column
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True


# def interface():
#     inter_file = xlrd.open_workbook(
#         r"C:\Users\Qiao\PycharmProjects\interface_test\data\data.xlsx")
#     table = inter_file.sheet_by_index(0)
#     ele = table.cell(0, 1)
#     ele_value = ele.value
#     print("name = %s" % ele_value, "\t", "type = %s" % type(ele_value), "\n")
#     return ele_value
#
#
# if __name__ == "__main__":
#     interface()
