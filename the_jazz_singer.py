import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")



driver = webdriver.Chrome(options=options)
url = "https://www.imdb.com/"
driver.get(url)
time.sleep(3)

driver.find_element(By. XPATH, "/html/body/div[2]/nav/div[2]/label[2]").click()

time.sleep(3)

driver.find_element(By. XPATH, "/html/body/div[2]/nav/div[2]/aside/div/div[2]/div/div[3]/span/div/div/ul/a[1]/span").click()
                                

time.sleep(3)

driver.find_element(By. XPATH, "/html/body/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/span/div/div/div[2]/div[16]/span[4]/a" ).click()

time.sleep(3)

driver.find_element(By. XPATH, "/html/body/div[2]/div/div[2]/div[3]/div/div[1]/div[3]/span/div/div/div/div[2]/h3/div/div/div/div[2]/div[2]/div[2]/div[1]/span/span/a").click()

time.sleep(3)

Director_menu = driver.find_element(By. XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a" ).get_attribute("textContent")
Writers_menu = driver.find_element(By. XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[2]").get_attribute("outerText").split("\n")[1]    ##.split(")")[0:3]
Stars_menu = driver.find_element(By. XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]").get_attribute("outerText").split("\n")[1]
 


driver.find_element(By. XPATH, "/html/body/div[2]/nav/div[2]/a" ).click()

time.sleep(3)

driver.find_element(By. NAME, "q").send_keys("The Jazz Singer")

time.sleep(3)

driver.find_element(By. XPATH, "/html/body/div[2]/nav/div[2]/div[1]/form/div[2]/div/div/div/ul/li[1]" ).click()

time.sleep(3)



Director_homepage = driver.find_element(By. XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]" ).get_attribute("textContent")
Writers_homepage = driver.find_element(By. XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[2]").get_attribute("outerText").split("\n")[1]
Stars_homepage = driver.find_element(By. XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]").get_attribute("outerText").split("\n")[1]
 


if Director_menu == Director_homepage:
    print("Director correct")
else:
    print("Director dif")
if Writers_menu == Writers_homepage:
    print("Writes correct")
else:
    print("Writes dif")
if Stars_menu == Stars_homepage:
    print("Stars correct")
else: 
    print("Stars dif")



driver.find_element(By. XPATH, "/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[2]/div[1]/a" ).click()
time.sleep(5)

links = driver.find_elements(By.CSS_SELECTOR, "a")
links = links[0:(len(links)-2)]

image_links = []

for link in links:
    x = link.get_attribute("href")
    if x.startswith("https://www.imdb.com/title/tt0018037/mediaviewer/") == True:
        image_links.append(x)
        
for image_link in image_links:
    r = requests.head(image_link)
    if r.status_code == 200:
        print("Link is working")
    else:
        print(r.status_code, "\t", image_link)




driver.close()