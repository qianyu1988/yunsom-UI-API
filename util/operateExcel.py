# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-12
# @Author  : derek.zhang

import xlrd

from config.VarConfig import testdataPath


class OperateExcel():

    def __init__(self):
        self.workbook = None
        self.sheet = None


    def load_workbook(self, filename):
        '''
        加载excel 文件
        :param filename:
        :return:
        '''
        try:
            self.workbook = xlrd.open_workbook(filename)
        except Exception as e:
            raise e
        return self.workbook


    def get_sheet_by_name(self, sheetaname):
        '''
        根据sheetname 获取sheet
        :param sheetaname:
        :return:
        '''
        try:
            self.sheet = self.workbook.sheet_by_name(sheetaname)
        except Exception as e:
            raise e
        return self.sheet

    def get_sheet_by_index(self,sheetIndex):
        '''
        根据sheetindex 获取sheet
        :param sheetIndex:
        :return:
        '''
        try:
            self.sheet = self.workbook.sheet_by_index(sheetIndex)
        except Exception as e:
            raise e
        return self.sheet


    def get_row_values(self,row_num):
        try:
            values = self.sheet.row_values(row_num)
        except Exception as e:
            raise e
        return values

    def get_rows_num(self):
        return self.sheet.nrows


if __name__ == "__main__":
    excel = OperateExcel()
    excel.load_workbook(testdataPath)
    excel.get_sheet_by_name('login')
    row0_values = excel.get_row_values(0)
    row1_values = excel.get_row_values(1)
    values = dict(zip(row0_values,row1_values))
    print(values)
