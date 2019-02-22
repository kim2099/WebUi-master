from comm.webDriver import webDriver
#导入登录界面元素类
import pageElement.loginPage as loginPage
#导入后台主界面元素类
import pageElement.C_list_Page as C_list_Page
#导入公司详情界面元素类
import pageElement.C_detail_Page as C_detail_Page
#导入日志模块类
from comm.md_logger import myLog
#导入公共方法类
import comm.common as common
import paramunittest
import unittest
import time
add_corporateCase = common.get_excel_value('add_corporate')
@paramunittest.parametrized(*add_corporateCase)
class add_Corporate(webDriver,unittest.TestCase):
    def setParameters(self, case_Name, user_Name, user_Pwd, corporate_name, Corporate_Registration_No, text, result, reMarks):
        self.case_Name = case_Name
        self.user_Name = user_Name
        self.user_Pwd = user_Pwd
        self.corporate_name = corporate_name
        self.Corporate_Registration_No = Corporate_Registration_No
        self.text = text
        #self.file_Path = file_Path
        self.result = result
        self.reMark = reMarks
    def test_add_corporate(self):
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
        #点击添加按钮
        C_detail_Page.click_add(self.driver)
        time.sleep(2)
        # 输入公司name
        C_detail_Page.enter_corporate_name(self.driver,self.corporate_name,self.Corporate_Registration_No)
        # 点击创建按钮
        C_detail_Page.click_create(self.driver)
        time.sleep(5)
        actualresult = self.driver.find_element_by_xpath("//div[@class = 'alert alert-success']/b").text
        myLog.logger().info('实际输出结果:' + actualresult)
        myLog.logger().info('预期输出结果:' + self.text)
        self.assertEqual(actualresult, self.text, msg ="实际结果与预期不符测试失败")
        common.Screenshot1()








