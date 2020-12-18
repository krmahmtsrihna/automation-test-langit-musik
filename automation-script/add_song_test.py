from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
TEST CASE PERTAMA
'''

# Step 1) Open Chrome 
browser = webdriver.Chrome()

# Step 2) Navigate to Langit Musik
browser.get("https://www.langitmusik.co.id/")

# Step 3) Click Upload Lagu
uploadlagu = browser.find_element_by_xpath("//span[normalize-space()='Upload Lagu']")
uploadlagu.click()

# Step 4) Cek Elemen Button Gabung Sekarang
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='GABUNG SEKARANG']")))

wait = WebDriverWait( browser, 5 )
browser.quit()

'''
TEST CASE KEDUA
'''

# Step 1) Open Chrome 
browser = webdriver.Chrome()

# Step 2) Navigate to Langit Musik
browser.get("https://laguku.id/")

# Step 3) Click Gabung Sekarang
gabung_sekarang = browser.find_element_by_xpath("//button[normalize-space()='GABUNG SEKARANG']")
gabung_sekarang.click()

# Step 4) Enter Username & Password
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='ENTER YOUR USERNAME']")))
username = browser.find_element_by_xpath("//input[@placeholder='ENTER YOUR USERNAME']")
password = browser.find_element_by_xpath("//input[@placeholder='TYPE YOUR PASSWORD']")
username.send_keys("wulanhilmira")
password.send_keys("whrwhrwhr")
submit = browser.find_element_by_xpath("//button[normalize-space()='MASUK']")

# Step 5) Click Login to Submit
submit.click()

# Step 6) Click Menu Album
album = browser.find_element_by_xpath("//a[@ui-sref='album']")
album.click()

# Step 7) Click view pada album yang ingin ditambahkan lagu
wait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View']")))
album_name = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div/div[4]/div[2]/table/tbody/tr/td[2]").text
view_album = browser.find_element_by_xpath("//span[normalize-space()='View']")
view_album.click()

# Step 8) Click Add Song
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Add Song']")))
add_song = browser.find_element_by_xpath("//button[normalize-space()='Add Song']")
add_song.click()

# Step 9) Click New
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='New']")))
new_song = browser.find_element_by_xpath("//button[normalize-space()='New']")
new_song.click()

# step 10) Check typo
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[1]/label/b[1]")))
field = {
	"Song Name" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[1]/label/b[1]"),
	"Song Name Original" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[2]/label/b"),
	"Album Name" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[3]/label/b[1]"),
	"Artist Name" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[4]/label/b[1]"),
	"Genre" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[5]/label/b[1]"),
	"Issue Date" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[6]/label/b[1]"),
	"Unique Search Keyword" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[7]/label/b[1]"),
	"Hit Song" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[1]/label[1]/b"),
	"Adult Only" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[1]/label[2]/b"),
	"Stream" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[2]/label[1]/b"),
	"MP3 Download" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[2]/label[2]/b"),
	"Instrument" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[3]/label[1]/b"),
	"Main Song" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[3]/label[2]/b"),
	"Track No" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[4]/label/b[1]"),
	"Label Song Code (ISRC)" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[5]/label/b[1]"),
	"Price" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[7]/label/b[1]"),
	"Lyric **" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[8]/label/b"),
	"Audio (wav/mp3)" : browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[2]/form/div[9]/label[2]/b[1]")
}
print("TEST CASE : CHECK TYPO NAMA FIELD\n")
for i in field:
	print("Expected nama field : ", i)
	print("Actual nama field : ", field[i].text)
	print("Status : ", field[i].text == i)
	print("==============================================")

wait = WebDriverWait( browser, 5 )
browser.quit()


'''
TEST CASE KETIGA
'''

# Step 1) Open Chrome 
browser = webdriver.Chrome()

# Step 2) Navigate to Langit Musik
browser.get("https://laguku.id/")

# Step 3) Click Gabung Sekarang
gabung_sekarang = browser.find_element_by_xpath("//button[normalize-space()='GABUNG SEKARANG']")
gabung_sekarang.click()

# Step 4) Enter Username & Password
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='ENTER YOUR USERNAME']")))
username = browser.find_element_by_xpath("//input[@placeholder='ENTER YOUR USERNAME']")
password = browser.find_element_by_xpath("//input[@placeholder='TYPE YOUR PASSWORD']")
username.send_keys("wulanhilmira")
password.send_keys("whrwhrwhr")
submit = browser.find_element_by_xpath("//button[normalize-space()='MASUK']")

# Step 5) Click Login to Submit
submit.click()

# Step 6) Click Menu Album
album = browser.find_element_by_xpath("//a[@ui-sref='album']")
album.click()

# Step 7) Click view pada album yang ingin ditambahkan lagu
wait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View']")))
album_name = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div/div[4]/div[2]/table/tbody/tr/td[2]").text
view_album = browser.find_element_by_xpath("//span[normalize-space()='View']")
view_album.click()

# Step 8) Click Add Song
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Add Song']")))
add_song = browser.find_element_by_xpath("//button[normalize-space()='Add Song']")
add_song.click()

# Step 9) Click New
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='New']")))
new_song = browser.find_element_by_xpath("//button[normalize-space()='New']")
new_song.click()

# step 10) Check empty save
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@ng-click='saveSong()']")))
save_button = browser.find_element_by_xpath("//button[@ng-click='saveSong()']")
save_button.click()
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[12]/div/div/div[1]/div")))
notif = browser.find_element_by_xpath("/html/body/div[12]/div/div/div[1]/div")
print("TEST CASE : CHECK EMPTY ADD SONG FORM SAVE")
if notif.text != "Silahkan diisi kolom Song Name":
	print("FAILED")
else:
	print("SUCCESS")
print("=============================================")
ok_button = browser.find_element_by_xpath("//button[normalize-space()='OK']")
ok_button.click()
close_button = browser.find_element_by_xpath("//div[@id='songsModal']//b[contains(text(),'X')]")
close_button.click()

wait = WebDriverWait( browser, 5 )
browser.quit()

'''
TEST CASE KEEMPAT
'''

# Step 1) Open Chrome 
browser = webdriver.Chrome()

# Step 2) Navigate to Langit Musik
browser.get("https://laguku.id/")

# Step 3) Click Gabung Sekarang
gabung_sekarang = browser.find_element_by_xpath("//button[normalize-space()='GABUNG SEKARANG']")
gabung_sekarang.click()

# Step 4) Enter Username & Password
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='ENTER YOUR USERNAME']")))
username = browser.find_element_by_xpath("//input[@placeholder='ENTER YOUR USERNAME']")
password = browser.find_element_by_xpath("//input[@placeholder='TYPE YOUR PASSWORD']")
username.send_keys("wulanhilmira")
password.send_keys("whrwhrwhr")
submit = browser.find_element_by_xpath("//button[normalize-space()='MASUK']")

# Step 5) Click Login to Submit
submit.click()

# Step 6) Click Menu Album
album = browser.find_element_by_xpath("//a[@ui-sref='album']")
album.click()

# Step 7) Click view pada album yang ingin ditambahkan lagu
wait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View']")))
album_name = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div/div[4]/div[2]/table/tbody/tr/td[2]").text
view_album = browser.find_element_by_xpath("//span[normalize-space()='View']")
view_album.click()
# Step 8) Click Add Song
wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Add Song']")))
add_song = browser.find_element_by_xpath("//button[normalize-space()='Add Song']")
add_song.click()

# Step 9) Click New
# wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='New']")))
# new_song = browser.find_element_by_xpath("//button[normalize-space()='New']")
# new_song.click()

#step 10) Check Error Handling Form

test_cases = [
	"Less than 5 keyword",
	"form input only space",
	"right input",
]

print("TEST CASE : CHECK ERROR HANDLING ADD SONG FORM")

wait = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='New']")))
new_song = browser.find_element_by_xpath("//button[normalize-space()='New']")
new_song.click()


wait = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[1]/div/input")))
songname = browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[1]/div/input")
genre = browser.find_element_by_xpath("//select[@class='form-control ng-pristine ng-untouched ng-valid ng-empty']")
issuedate = browser.find_element_by_xpath("//*[@id=\"songsModal\"]/div/div/div[2]/div/div[1]/form/div[6]/div/div/input")
keyword = browser.find_element_by_xpath("//textarea[@class='form-control ng-pristine ng-untouched ng-valid ng-empty']")
generate = browser.find_element_by_xpath("//button[normalize-space()='Generate']")
lyric = browser.find_element_by_xpath("//button[normalize-space()='Tambah']")
upload = browser.find_element_by_xpath("//div[@class='form-group']//div[@class='col-sm-9']//div//div[@class='form-group']//button[@type='submit'][normalize-space()='Upload']")
save = browser.find_element_by_xpath("//button[@ng-click='saveSong()']")

print("scene : Input right song")
songname.send_keys("test_song : Input right song")
genre.send_keys("Anak-anak")
issuedate.send_keys("11/12/2020")
keyword.send_keys("keyword 1 keyword 1, keyword 2, keyword 3 keyword 3")
generate.click()
lyric.click()
wait = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"lyricsModal\"]/div/div/div[2]/div/div/div/div/div[2]/div[3]/div[3]")))
isi_lyric = browser.find_element_by_xpath("//*[@id=\"lyricsModal\"]/div/div/div[2]/div/div/div/div/div[2]/div[3]/div[3]")
isi_lyric.click()
isi_lyric.send_keys("test lyric")
save_lyric = browser.find_element_by_xpath("//button[normalize-space()='SAVE']")
save_lyric.click()
wait = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//label[@for='upload-mp3']")))
browse = browser.find_element_by_xpath("//*[@id=\"upload-mp3\"]")
browse.send_keys('C:/Users/IDX-171/Documents/dti hana/audiotest.mp3')
upload.click()
wait = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='OK']")))
browse_ok = browser.find_element_by_xpath("//button[normalize-space()='OK']")
browse_ok.click()
wait = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[@ng-click='saveSong()']")))
save.click()
try:
	wait = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Yes']")))
	yes_save = browser.find_element_by_xpath("//button[normalize-space()='Yes']")
	yes_save.click()
	wait = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='OK']']")))
	saved_notif = browser.find_element_by_xpath("/html/body/div[11]/div/div/div[1]/div").text
	ok_save = browser.find_element_by_xpath("//button[normalize-space()='OK']")
	ok_save.click()
	print("Expected result : Data berhasil disimpan")
	print("Actual result : ", saved_notif)
	if actual_result == "Data berhasil disimpan":
		print("Status : SUCCESS")
	else:
		print("Status : FAILED")
except:
	print("Status : FAILED")
print("===========================================================")


wait = WebDriverWait( browser, 5 )
page_title = browser.title

browser.quit()
