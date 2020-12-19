from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Step 1) Open Chrome 
browser = webdriver.Chrome()

# Step 2) Navigate to Langit Musik
browser.get("https://www.langitmusik.co.id/")

# Step 3) Click Login Button
login = browser.find_element_by_xpath("//a[normalize-space()='LOG IN']")
login.click()

# Step 4) Enter MSISDN & Password
msisdn = browser.find_element_by_xpath("//input[@id='msisdn']")
password = browser.find_element_by_xpath("//input[@id='pwd']")
msisdn.send_keys("081234567891")
password.send_keys("sq0213sq0213")
submit = browser.find_element_by_xpath("//button[normalize-space()='LOGIN']")

# Step 5) Click Login to Submit
submit.click()

wait = WebDriverWait( browser, 5 )