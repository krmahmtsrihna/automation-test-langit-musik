from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://www.langitmusik.co.id/")

promo = browser.find_element_by_xpath("//span[normalize-space()='Promo']")
promo.click()

wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Program LM Musik Hits 2020']")))

promo_item = browser.find_element_by_xpath("//a[normalize-space()='Program LM Musik Hits 2020']")
promo_item.click()

try:
	wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Program LM Musik Hits 2020']")))
	print("SUCCESS")
except:
	print("FAILED")
	
wait = WebDriverWait(browser, 5)
browser.quit()

