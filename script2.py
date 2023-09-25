from selenium.webdriver import Chrome
import time
path="//Users//omar//Desktop//chromedriver"
driver = Chrome(executable_path=path)
driver.get("https://cp.lfchosting.com/index.php?Function=Email")
driver.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td[3]/form/table/tbody/tr/td/table[1]/tbody/tr[4]/td[2]/input").send_keys("bakkali")
driver.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td[3]/form/table/tbody/tr/td/table[1]/tbody/tr[5]/td[2]/input").send_keys("poker123")
driver.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td[3]/form/table/tbody/tr/td/table[1]/tbody/tr[6]/td[2]/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/table[3]/tbody/tr/td[3]/table[1]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/input").click()
for i in range(10) : #Hna atbdel ra9m li bghiti
 driver.find_element_by_xpath("/html/body/div[1]/table[3]/tbody/tr/td[3]/table[1]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[8]/td[2]/a").click()
 time.sleep(1)
 driver.find_element_by_xpath("/html/body/div[1]/table[3]/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input").send_keys("Simo_Test"+str(i))#hna adir smya li bghiti
 driver.find_element_by_xpath("/html/body/div[1]/table[3]/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/input").click()
 time.sleep(1)
 driver.find_element_by_xpath("/html/body/div[1]/table[3]/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input").send_keys("Iu4oechi")
 driver.find_element_by_xpath("/html/body/div[1]/table[3]/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/input").send_keys("Iu4oechi")
 driver.find_element_by_xpath("/html/body/div[1]/table[3]/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/input").click()
 driver.find_element_by_xpath("/html/body/div[1]/table[3]/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/input").click()
