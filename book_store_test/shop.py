from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
account = driver.find_element_by_link_text("My Account")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("nikita-rumin@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("autotest115062")
login = driver.find_element_by_name("login")
login.click()
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
html_5_forms_book = driver.find_element_by_css_selector(".post-181 > a > h3")
html_5_forms_book.click()
book_title = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title"), 'HTML5 Forms'))
driver.quit()






from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
account= driver.find_element_by_link_text("My Account")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("nikita-rumin@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("autotest115062")
login = driver.find_element_by_name("login")
login.click()
shop = driver.find_element_by_link_text("Shop")
shop.click()
html = driver.find_element_by_link_text("HTML")
html.click()
items = driver.find_elements_by_css_selector("a>h3")
if len(items) == 3:
print("В категории 3 товара")
else:
print("В категории неверно указано количество товаров: " + str(len(items)))
driver.quit()




from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
account = driver.find_element_by_link_text("My Account")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("nikita-rumin@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("autotest115062")
login = driver.find_element_by_name("login")
login.click()
shop = driver.find_element_by_link_text("Shop")
shop.click()
item_selector = driver.find_element_by_name("orderby")
items_selector_default = item_selector.get_attribute("value")
if items_selector_default == "menu_order":
print("Выбрана сортировка по умолчанию")
else:
print("Выбрана сортировка НЕ по умолчанию")
select = Select(item_selector)
select.select_by_value("price-desc")
items_selector = driver.find_element_by_name("orderby")
items_selector_low = items_selector.get_attribute("value")
if items_selector_low == "price-desc":
print("Выбрана сортировка по убыванию")
else:
print("Выбрана сортировка по возрастанию")
driver.quit()





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
account = driver.find_element_by_link_text("My Account")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("test@email.com")
password = driver.find_element_by_id("password")
password.send_keys("SomeHardPassword123!@#!@#")
login = driver.find_element_by_name("login")
login.click()
shop = driver.find_element_by_link_text("Shop")
shop.click()
android_quick_start = driver.find_element_by_css_selector(".post-169 h3")
android_quick_start.click()
old_price = driver.find_element_by_css_selector(".price > del > span")
old_price_text = old_price.text
new_price = driver.find_element_by_css_selector(".price > ins > span")
new_price_text = new_price.text
assert old_price_text == "₹600.00"
assert new_price_text == "₹450.00"
book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a")))
book_cover.click()
book_cover_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
book_cover_close.click()






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 > a h3")
html5_webapp_development_book.click()
html5_webapp_development_book_add_btn = driver.find_element_by_css_selector(".single_add_to_cart_button")
html5_webapp_development_book_add_btn.click()
basket_item_value = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
basket_item_value_text = basket_item_value.text
assert basket_item_value_text == "1 Item"
basket_value = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
basket_value_text = basket_value.text
assert basket_value_text == "₹180.00"
basket = driver.find_element_by_class_name("wpmenucart-contents")
basket.click()
subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
total_price = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹189.00"))
driver.quit()





from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
driver.execute_script("window.scrollBy(0, 300);")
html5_book = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
html5_book.click()
time.sleep(3)
html5_bookk = driver.find_element_by_css_selector(".post-180 .add_to_cart_button")
html5_bookk.click()
basket = driver.find_element_by_class_name("wpmenucart-contents")
basket.click()
time.sleep(3)
first_item = driver.find_element_by_class_name("remove")
first_item.click()
undo = driver.find_element_by_link_text("Undo?")
undo.click()
quantity = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
quantity.clear()
quantity.send_keys("3")
update_basket = driver.find_element_by_name("update_cart")
update_basket.click()
quantity = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
quantity_value = quantity.get_attribute("value")
assert quantity_value == '3'
time.sleep(3)
coupon = driver.find_element_by_name("apply_coupon")
coupon.click()
error = driver.find_element_by_css_selector(".woocommerce-error")
error = error.text
assert error == 'Please enter a coupon code.'



