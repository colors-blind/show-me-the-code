#coding=utf-8

from pandas import DataFrame
from yaml import load
from collections import OrderedDict


def read_data(file_name):

    """
        从txt文件读取数据，返回字典数据
    """

    try:

        with open(file_name) as fd:
            data = load(fd.read())
            od = OrderedDict(data)

        return data

    except Exception as error:
        print error
        return None


def write_data(data):

    """
        写数据到Excel表格
    """

    if not data:
        print 'Empty data...'
        return None

    try:
        index_column = data.keys()
        data_column = data.values()

        for index, columns in enumerate(data_column):
            columns.insert(0, index_column[index])

        df = DataFrame(data_column)
        df.to_excel('test.xlsx', sheet_name='sheet1', index=False, header=None)

    except Exception as error:
        print error

    return "Success"


if __name__ == '__main__':

    data = read_data('student.txt')
    res = write_data(data)
    print 'write res', res

