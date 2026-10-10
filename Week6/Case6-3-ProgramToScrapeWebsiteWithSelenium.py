from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://nureh.pk/collections/new-in"

cService = webdriver.ChromeService(executable_path='C:\\Users\\HP\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe') # '/Users/bpfalz/Downloads/chromedriver' for my macbook
driver = webdriver.Chrome(service=cService)

driver.get(url)

qouestList=[]
qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 't4s-product t4s-pr-grid t4s-pr-style1 t4s-pr-')]")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    innera = qoutesDiv[p+1].find_element(By.TAG_NAME, "a")
    quote["img"] =innerImg.get_attribute('src') 
    quote["lines"] =innerImg.get_attribute('alt') 
    quote['url'] = innera.get_attribute('href')
    qouestList.append(quote)

filename = 'Week4/inspirational_quotesMethod2.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['url','img','lines','author'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()