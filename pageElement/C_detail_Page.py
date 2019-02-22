
import comm.common as common

#点击创建按钮
def click_add(driver):
    driver.find_element_by_xpath('//*[@id="add_corporate_btn"]').click()
#点击取消按钮
def click_cancel(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[5]/a/button').click()
#输入公司名字和公司ID
def enter_corporate_name(driver,corporate_name,corporate_registration_number):
    driver.find_element_by_name('corporate_name').send_keys(corporate_name)
    driver.find_element_by_name('corporate_registration_number').send_keys(corporate_registration_number)
def click_create(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[5]/button').click()

