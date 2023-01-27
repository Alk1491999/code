import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Webdriverwait
from selenium.webdriver.support import expected_condition as EC
from selenium.webdriver.common.by import By

#below is the chrome driver
input_file = pd.Dataframe()
input_file["NAME"] = None
input_file["COST"] = None
driverpath = webdriver.chrome("C:\Program Files (x86)\selenium client\chromedriver.exe")
driverpath.get("https://www.flipkart.com/")
time.sleep(10)
Webdriverwait(driverpath, 50).until(EC.visibility_of_element_located(By.XPATH, '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').sendkeys("Mobiles")

Webdriverwait(driverpath, 50).until(EC.visibility_of_element_located(By.XPATH, '').sendkeys("Mobiles")
for i in range(2):
    input_file[i, "NAME"] = Webdriverwait(driverpath, 50).until(EC.visibility_of_element_located(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
    input_file[i, "COST"] = Webdriverwait(driverpath, 50).until(EC.visibility_of_element_located(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
input_file.to_excel("C:\Users\Alkesh\Desktop\mobile.xlsx")
