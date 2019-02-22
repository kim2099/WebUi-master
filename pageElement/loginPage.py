"""
登陆界面的元素
"""
from comm.md_logger import myLog
import comm.common as common
#登录名
def setUserName(driver,userName):
    myLog.logger().info('use_name:driver %s', driver)
    driver.find_element_by_name('userID').send_keys(userName)
#登录密码
def setUserPwd(driver, userPwd):
    driver.find_element_by_name('password').send_keys(userPwd)
#登录按钮
def click_login(driver):
    driver.find_element_by_id('submitLogin').click()
#判断是否登录成功
#退出登录
def click_exit(driver):
    driver.find_element_by_xpath('//*[@id="logout"]').click()
#登录名错误的的文案
def userName_Error(driver):
    userName_Text = driver.find_element_by_xpath("//form[@id='formLogin']/span[1]").text
    return userName_Text
