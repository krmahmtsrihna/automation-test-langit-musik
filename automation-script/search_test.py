from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from difflib import SequenceMatcher

keys = {
	"search dengan keyword berupa huruf (Valid)" : "From Home",
	"search dengan keyword berupa angka (Valid)" : "4581",
	"search dengan keyword berupa tanda baca (Valid)" : "???",
	"search dengan keyword berupa kombinasi huruf dan angka (Valid)" : "11 Januari",
	"search dengan keyword berupa kombinasi huruf dan tanda baca (Valid)" : "FRIENDS (Acoustic)",
	"search dengan keyword berupa kombinasi angka dan tanda baca (Valid)" : "22!.,",
	"search dengan keyword berupa kombinasi huruf, angka, dan tanda baca (Valid)" : "Back 2 U (AM 01:27)",
	"search dengan keyword yang mengandung tanda garis miring (Invalid)" : "1/3",
	"search dengan keyword berupa satu karakter (Invalid)" : "A",
	"search dengan keyword beruba huruf non-alphabet" : "もしもまたいつか"
}

for i in keys:
	browser = webdriver.Chrome(executable_path="chromedriver.exe")
	test_case_name = "test case : " + str(i)
	browser.get("https://www.langitmusik.co.id/")
	search = browser.find_element_by_xpath("//input[contains(@placeholder,'Search')]")
	search.send_keys(keys[i])
	try:
		wait = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[2]/div/main/div/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div[1]/a[1]")))
		result = browser.find_element_by_xpath("//*[@id=\"content\"]/div[2]/div/main/div/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div[1]/a[1]")
	except:
		# wait = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[2]/div/main/div/div/div[1]/div/div/div[2]")))
		# result = browser.find_element_by_xpath("//*[@id=\"content\"]/div[2]/div/main/div/div/div[1]/div/div/div[2]")
		result = ""

	search_result = result.text.split("\n")[0] if result != "" else ""
	result_check = True
	if search_result != "":
		if 0.80 > SequenceMatcher(None, search_result,keys[i]).ratio():
			search_result_words = search_result.split(" ")
			for j in keys[i].split(" "):
				if j not in search_result_words:
					result_check = False
					break

	print(test_case_name)
	print("Search Input : ",keys[i])
	print("Search result : ", search_result)
	if search_result == "" or result_check == True:
		if search_result != "":
			print("Similarity ratio : ", SequenceMatcher(None, search_result,keys[i]).ratio())
		print("SUCCESS")
	else:
		print("Similarity ratio : ", SequenceMatcher(None, search_result,keys[i]).ratio())
		print("FAILED")

	print("==========================================================")

	wait = WebDriverWait(browser, 5)
	browser.quit()

