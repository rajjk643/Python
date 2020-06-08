import getpass
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#cope
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

insta_username = "the_word_blotter"
insta_password = "Rachel@69"
browser = webdriver.Chrome()
url = "https://www.instagram.com/"
browser.get(url)

time.sleep(2)
username_el = browser.find_element_by_name("username")
username_el.send_keys(insta_username)

password_el = browser.find_element_by_name("password")
# entering password in hidden way
#insta_password = getpass.getpass("Enter Password : \n")
password_el.send_keys(insta_password)

submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()

body_el = browser.find_element_by_css_selector("body")
html_text = body_el.get_attribute("innerHTML")

savenotNowButton = WebDriverWait(browser, 15).until(
    lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')
)
savenotNowButton .click()

notNowButton = WebDriverWait(browser, 15).until(
    lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')
)
notNowButton .click()

# comment
# comment= "Awesome !!"
# comment_xpath_str = "//textarea[contains(@placeholder,'Add a comment')]"
# comment_el = browser.find_elements_by_xpath(comment_xpath_str)
# for btn in comment_el:
#     time.sleep(2)
#     try:
#         comment_el.send_keys(comment)
#         submit_btns_xpath = "//button[contains(text(),'Post')]"
#         submit_btn_els = browser.find_element_by_xpath(submit_btns_xpath)
#         submit_btn_els.click()
#     except:
#         pass

# comment_box = ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
# browser.execute_script("arguments[0].scrollIntoView(true);", comment_box)
# comment_box.send_keys("Hello!")
for i in range(6):
    commentArea = browser.find_element_by_class_name('Ypffh')
    commentArea.click()
    commentArea = browser.find_element_by_class_name('Ypffh')
    commentArea.send_keys("YOUR COMMENT HERE...")
    submit_btns_xpath = "//button[contains(text(),'Post')]"
    submit_btn_els = browser.find_element_by_xpath(submit_btns_xpath)
    submit_btn_els.click()
