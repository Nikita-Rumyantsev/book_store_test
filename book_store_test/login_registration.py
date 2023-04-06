from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
account = driver.find_element_by_link_text("My Account")
account.click()
email = driver.find_element_by_id("reg_email")
email.send_keys("nikita-rumin@mail.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("autotest115062")
register = driver.find_element_by_name("register")
register.click()
driver.quit()




from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
account = driver.find_element_by_link_text("My Account")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("test@email.com")
password_ = driver.find_element_by_id("password")
password.send_keys("SomeHardPassword123!@#!@#")
login = driver.find_element_by_name("login")
login.click()
driver.quit()




