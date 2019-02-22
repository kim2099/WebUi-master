"""
该类主要是存放一些公共方法，比如：元素查找、截屏
、操作Excel等等
"""
#导入日志模块
from comm.md_logger import myLog

#导入截图模
from PIL import ImageGrab
#读excel模块
import xlrd
import time
import shutil
import os
'''
filePath:current path
qr：file name format
'''
filePath = os.path.split(os.path.dirname(__file__))[0]
'''
find element
flag:True or Flase
xpath:element xpath
'''

'''
Screenshot function
imPath:picture save path
imType: picture type
'''
def Screenshot(imPath,imType):
    im = ImageGrab.grab()
    im.save(imPath, imType)

def Screenshot1():
    rq = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    # log文件的存放路径
    imPath = filePath + '/result/image/' + rq + '.png'
    im = ImageGrab.grab()
    im.save(imPath)
def Screenshot2(imPath):
    im = ImageGrab.grab()
    im.save(imPath)
'''
Delete folder content
path: folder path
'''
def delFile(path):
    shutil.rmtree(path)
    os.makedirs(path)
'''
excel_name:excel file name
sheet_name:sheet name
return:sheet value
'''
def get_excel_value(sheet_name):
    cls = []
    excel_path = filePath + '/data/testCase.xls'
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_Name':
            cls.append(sheet.row_values(i))
    return cls
    #获取查询后table的行数以及列数
# def get_table_value(self,table_ID,driver,search_Id):
    # table = driver.find_element_by_id(table_ID)
    # table_rows = table.find_elements_by_tag_name("tr")
    # table_cols = table.find_elements_by_tag_name("th")
    # if len(table_rows) >= 1:
        # table_num = 1
        # for table_num in (1,len(table_rows)):
            # table_text = table_rows[table_num].find_elements_by_tag_name('td')[1].text
            # isExist = self.assertTrue(search_Id in table_text)
    # #else print "There is not record!
    # return isExist