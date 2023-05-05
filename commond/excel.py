# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2023/3/22 16:29
# @File: excel.py

import xlwings


class Excel(object):
    """
    操作excel
    """

    # 定义结构函数，创建对象自动执行

    def __init__(self, file_path=None, sheet_id=None, sheet_name=None):
        """
        :param file_path: 如果没传值，默认为excel路径
        :param sheet_id: 如果没传值，默认为第一个索引为0的第一个sheet
        ：param sheet_name : 如果没传值，默认为sheet1名字的sheet页
        """

        if file_path:
            self.file_path = file_path
            self.sheet_id = sheet_id
        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0
        if sheet_name is not None:
            self.sheet_name = sheet_name
        else:
            self.sheet_name = "Sheet1"

        self.app = xlwings.App(visible=False, add_book=False)
        if file_path:
            self.wb = self.app.books.open(self.file_path)
        else:
            self.wb = self.app.books.add()

        # self.sheet_table = self.active_sheet()

    # 成员方法
    # 获取sheet页操作对象，首先会检索sheet_name
    def active_sheet(self, sheet_name=None, sheet_index=None):
        """
        激活某个sheet
        :param sheet_name:
        :param sheet_index:
        :return:
        """

        # 如果存在
        if sheet_name:
            self.sheet_name = sheet_name
            sheet_table = self.wb.sheets[self.sheet_name]
        elif sheet_index:
            self.sheet_id = sheet_index
            sheet_table = self.wb.sheets[self.sheet_id]
            self.sheet_name = sheet_table.name
        else:
            sheet_table = self.wb.sheets[self.sheet_name]
        self.sheet_table = sheet_table
        return sheet_table

    def copy_sheet(self, sheet_name, new_sheet_name):
        sht = self.wb.sheets[sheet_name]
        sht.api.Copy(Before=sht.api)
        sht = self.wb.sheets[sheet_name + ' (2)']
        sht.name = new_sheet_name
        self.sheet_table = sht
        self.sheet_name = new_sheet_name
        return sht

    # 获取sheet页的行数
    @property
    def rows(self):
        return self.sheet_table.used_range.last_cell.row

    # 获取实例化sheet页的列数
    @property
    def cols(self):
        return self.sheet_table.used_range.last_cell.colum

    # 保存当前的excel， 默认为源文件，输入file_name 另存为新文件
    def save_excel(self, file_name=None):
        if file_name is None:
            self.wb.save(self.file_path)
        else:
            self.wb.save(file_name)
            self.file_path = file_name

    def close_excel(self, file_name=None):
        if file_name:
            self.save_excel(file_name)
        else:
            self.save_excel()
        self.wb.close()
        self.app.kill()

    # 新建sheet页，默认为最后一页，index为新建索引值
    def create_sheet(self, sheet_name=None):
        self.sheet_table = self.wb.sheets.add()
        if sheet_name:
            self.sheet_table.name = sheet_name
        # self.save_excel()

    def remove_cell(self, Range):
        self.sheet_table[Range].delete()

    # 删除列
    def remove_col(self, index):
        self.sheet_table[index[1]:index[1]].delete()
        # self.save_excel()

    # 删除行
    def remove_row(self, index):
        self.sheet_table[index[0]:index[0]].delete()
        # self.save_excel()

    # 获取某一个单元格的值
    def get_cell_value(self, row, col):
        if type(row) == str:
            return self.sheet_table.range(row).value
        else:
            return self.sheet_table.range(row, col).value

    # 通过value值索引excel位置
    def find_index_by_value(self, value):
        pass

    # 赋值excel某个行列值
    def insert_value_by_index(self, value, row=None, col=None, range_=None):
        if range_:
            self.sheet_table.range(range_).value = value
        elif row and col:
            self.sheet_table.cell(row, col).value = value
        else:
            raise ValueError('range_,col,row is not None')

    def insert_value_by_col(self, value, range_):
        self.sheet_table.range(range_).options(transpose=True).value = value

    def copy_coll(self, old_cell1, new_cell1, old_cell2=None, new_cell2=None, sheet_name=None, new_sheet_name=None):
        """
        辅助单元格内容样式到其他位置
        :param new_sheet_name: 目标sheet对象
        :param sheet_name: 源sheet对象
        :return:
        """
        # 将获取到的行，连同单元格样式，一起复制到resultsheet中
        self.sheet_table.range(old_cell1, old_cell2).copy(self.sheet_table.range(new_cell1, new_cell2))


if __name__ == '__main__':
    my_excle = Excel(r'F:\git\crowd_sourcing_auto_test_tool\Template\感知自动化测试工具输出表格.xlsx',
                     sheet_name='场景汇总结果')
    my_excle.copy_coll(1, 2, 3, 3)
    my_excle.wb.save()
    my_excle.wb.close()
    my_excle.app.kill()
