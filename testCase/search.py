from comm.webDriver import webDriver
#导入登录界面元素类
import pageElement.loginPage as loginPage
#导入后台主界面元素类
import pageElement.C_list_Page as C_list_Page
#导入日志模块类
from comm.md_logger import myLog
#导入公共方法类
import comm.common as common
import paramunittest
import unittest
import time
searchCase = common.get_excel_value('search')
@paramunittest.parametrized(*searchCase)
class searchCorporate(webDriver,unittest.TestCase):
    def setParameters(self, case_Name, user_Name, user_Pwd, search_name, result, reMarks):
        self.case_Name = case_Name
        self.user_Name = user_Name
        self.user_Pwd = user_Pwd
        self.search_name = search_name
        #self.file_Path = file_Path
        self.result = result
        self.reMark = reMarks
    def test_search(self):
        # 设置用例名称
        self._testMethodDoc = self.case_Name
        myLog.logger().info('测试用例名称:' + self._testMethodDoc)
        myLog.logger().info('测试用例说明:' + self.reMark)
        loginPage.setUserName(self.driver, self.user_Name)
        loginPage.setUserPwd(self.driver, self.user_Pwd)
        loginPage.click_login(self.driver)
        time.sleep(5)
        isLogin = loginPage.isLogin(self.driver)
        # 点击导航栏
        C_list_Page.click_Corporate_btn(self.driver)
        time.sleep(2)
        # 搜索框内输入公司name
        C_list_Page.input_corporate_Id(self.driver, self.search_name)
        # 点击查询按钮
        C_list_Page.click_Search_btn(self.driver)
        if self._testMethodDoc == 'test_search1':
            time.sleep(5)
            try:
                myLog.logger().info("实际输出结果:%s",C_list_Page.isSearch(self.driver))
                myLog.logger().info("预期输出结果 %s",self.search_name)
                self.assertEquals(C_list_Page.isSearch(self.driver),self.search_name)
                common.Screenshot1()
                myLog.logger().info("%s查询成功",C_list_Page.isSearch(self.driver))
            except Exception as e:
                common.Screenshot1()
                myLog.logger().info("查询失败 %s",e)
        elif self._testMethodDoc == 'test_search2':
            try:
                self.assertEquals(C_list_Page.isSearch(self.driver), self.search_name)
            except Exception as e:
                common.Screenshot1()
                myLog.logger().info("查询成功 %s",e)





