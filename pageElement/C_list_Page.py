#后台主界面元素
import comm.common as common
#点击导航栏
def click_Corporate_btn(driver):
    driver.find_element_by_xpath('//*[@id="corporate"]').click()
#搜索框内输入公司ID
def input_corporate_Id(driver, id):
    driver.find_element_by_id('search_one').send_keys(id)
#搜索框内输入公司名字
def input_corporate_Name(driver, name):
    driver.find_element_by_id('search_one').send_keys(name)
#选择筛选状态条件
def select_Status(driver, status):
    driver.find_element_by_id('search_two').select_by_visile_text(status)
#点击查询按钮
def click_Search_btn(driver):
    driver.find_element_by_id('search').click()
#判断是否登录成功
#0:xpath 1:id 2:name
def isSearch(driver):
    isExist = common.isElementExist(0, driver, '/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[3]')
    return isExist
#清除查询按钮
def click_Clear_btn(driver):
    driver.find_element_by_class('btn btn-cancel align-l-10').click()
#点击添加按钮
def add_corporate_btn(driver):
    driver.find_element_by_id('add_corporate_btn').click()
#点击查看按钮
def view_btn(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[8]/a').click()
#设定页面显示数目
def select_Number(driver, number):
    driver.find_element_by_id('page_limit').select_by_visile_text(number)
#点击跳转第二页
def click_scend_page(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[5]/div[2]/div/ul/li[4]/a').click()
#点击跳转下一页
def click_next_page(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[5]/div[2]/div/ul/li[8]/a').click()
#点击返回下一页
def click_previous_page(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[5]/div[2]/div/ul/li[2]/a').click()
#点击返回首页
def click_previous_page(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[5]/div[2]/div/ul/li[1]/a').click()
#点击跳转最后一页
def click_last_page(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[5]/div[2]/div/ul/li[7]/a').click()

