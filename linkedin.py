from selenium import webdriver

driver = webdriver.Chrome()

email = driver.find_element_by_id("login-email")
email.send_keys("zhouyiyang9508@gmail.com")

password = driver.find_element_by_id("login-password")
password.send_keys("******")

sign_in_button = driver.find_element_by_xpath('.//form[@type="submit"]')
sign_in_button.click()



