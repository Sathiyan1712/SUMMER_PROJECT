from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.support import expected_conditions as EC
import time

import pandas as pd

# Path to the geckodriver executable
geckodriver_path = 'C:\\Users\\satya\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe'


# Create a Service object
service = Service(geckodriver_path)

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service)

# Your subsequent code
driver.get("https://josaa.admissions.nic.in/applicant/SeatAllotmentResult/CurrentORCR.aspx")

#no disturbance to above code
round1=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlroundno_chosen")
time.sleep(1)
round1.click()
botton1_1=driver.find_element(By.XPATH, "//li[@data-option-array-index='1']")
time.sleep(1)
botton1_1.click()


insti_type=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstype_chosen")
time.sleep(1)
insti_type.click()
botton2=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[2]/div/div/div/ul/li[2]")
time.sleep(1)
botton2.click()



insti_name=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstitute_chosen")
time.sleep(1)
insti_name.click()
botton3=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[3]/div/div/div/ul/li[2]")
time.sleep(1)
botton3.click()


branch=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlBranch_chosen")
time.sleep(1)
branch.click()
botton4=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div/div/div/ul/li[2]")
time.sleep(1)
botton4.click()



category_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlSeattype_chosen")
time.sleep(1)
category_.click()
botton5=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[5]/div/div/div/ul/li[2]")
time.sleep(1)
botton5.click()




submit_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSubmit")
time.sleep(1)
submit_.click()

table1=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GridView1")
      

row1s = table1.find_elements(By.TAG_NAME, "tr")
header1s =table1.find_elements(By.TAG_NAME , "th")

title1s=[]
for i in header1s:
    title=i.text
    title1s.append(title)
df=pd.DataFrame(columns=title1s) 

data1 = []

for row in row1s[1:]:
    cells = row.find_elements(By.TAG_NAME, 'td')
    row_data1 = [cell.text for cell in cells]
    data1.append(row_data1)
    l=len(df)
    df.loc[l]=row_data1
print("success")
    
df.to_csv('Round_1.csv')





######ROUND----2

round2=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlroundno_chosen")
time.sleep(1)
round2.click()
botton2_1=driver.find_element(By.XPATH, "//li[@data-option-array-index='2']")
time.sleep(1)
botton2_1.click()


insti_type=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstype_chosen")
time.sleep(1)
insti_type.click()
botton2=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[2]/div/div/div/ul/li[2]")
time.sleep(1)
botton2.click()



insti_name=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstitute_chosen")
time.sleep(1)
insti_name.click()
botton3=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[3]/div/div/div/ul/li[2]")
time.sleep(1)
botton3.click()


branch=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlBranch_chosen")
time.sleep(1)
branch.click()
botton4=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div/div/div/ul/li[2]")
time.sleep(1)
botton4.click()



category_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlSeattype_chosen")
time.sleep(1)
category_.click()
botton5=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[5]/div/div/div/ul/li[2]")
time.sleep(1)
botton5.click()




submit_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSubmit")
time.sleep(1)
submit_.click()

table2=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GridView1")
      

row2s = table2.find_elements(By.TAG_NAME, "tr")
header2s =table2.find_elements(By.TAG_NAME , "th")

title2s=[]
for i in header2s:
    title=i.text
    title2s.append(title)
df=pd.DataFrame(columns=title2s) 

data2 = []

for row in row2s[1:]:
    cells = row.find_elements(By.TAG_NAME, 'td')
    row_data2 = [cell.text for cell in cells]
    data2.append(row_data2)
    l=len(df)
    df.loc[l]=row_data2
print("success")
    
df.to_csv('Round_2.csv')


#####ROUND----3


round3=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlroundno_chosen")
time.sleep(1)
round3.click()
botton3_1=driver.find_element(By.XPATH, "//li[@data-option-array-index='3']")
time.sleep(1)
botton3_1.click()


insti_type=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstype_chosen")
time.sleep(1)
insti_type.click()
botton2=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[2]/div/div/div/ul/li[2]")
time.sleep(1)
botton2.click()



insti_name=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstitute_chosen")
time.sleep(1)
insti_name.click()
botton3=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[3]/div/div/div/ul/li[2]")
time.sleep(1)
botton3.click()


branch=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlBranch_chosen")
time.sleep(1)
branch.click()
botton4=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div/div/div/ul/li[2]")
time.sleep(1)
botton4.click()



category_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlSeattype_chosen")
time.sleep(1)
category_.click()
botton5=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[5]/div/div/div/ul/li[2]")
time.sleep(1)
botton5.click()




submit_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSubmit")
time.sleep(1)
submit_.click()

table3=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GridView1")
      

row3s = table3.find_elements(By.TAG_NAME, "tr")
header3s =table3.find_elements(By.TAG_NAME , "th")

title3s=[]
for i in header3s:
    title=i.text
    title3s.append(title)
df=pd.DataFrame(columns=title3s) 

data3 = []

for row in row3s[1:]:
    cells = row.find_elements(By.TAG_NAME, 'td')
    row_data3 = [cell.text for cell in cells]
    data3.append(row_data3)
    l=len(df)
    df.loc[l]=row_data3
print("success")
    
df.to_csv('Round_3.csv')


####ROUND----4


round4=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlroundno_chosen")
time.sleep(1)
round4.click()
botton4_1=driver.find_element(By.XPATH, "//li[@data-option-array-index='4']")
time.sleep(1)
botton4_1.click()


insti_type=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstype_chosen")
time.sleep(1)
insti_type.click()
botton2=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[2]/div/div/div/ul/li[2]")
time.sleep(1)
botton2.click()



insti_name=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstitute_chosen")
time.sleep(1)
insti_name.click()
botton3=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[3]/div/div/div/ul/li[2]")
time.sleep(1)
botton3.click()


branch=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlBranch_chosen")
time.sleep(1)
branch.click()
botton4=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div/div/div/ul/li[2]")
time.sleep(1)
botton4.click()



category_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlSeattype_chosen")
time.sleep(1)
category_.click()
botton5=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[5]/div/div/div/ul/li[2]")
time.sleep(1)
botton5.click()




submit_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSubmit")
time.sleep(1)
submit_.click()

table4=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GridView1")
      

row4s = table4.find_elements(By.TAG_NAME, "tr")
header4s =table4.find_elements(By.TAG_NAME , "th")

title4s=[]
for i in header4s:
    title=i.text
    title4s.append(title)
df=pd.DataFrame(columns=title4s) 

data4 = []

for row in row4s[1:]:
    cells = row.find_elements(By.TAG_NAME, 'td')
    row_data4 = [cell.text for cell in cells]
    data4.append(row_data4)
    l=len(df)
    df.loc[l]=row_data4
print("success")
    
df.to_csv('Round_4.csv')


#### ROUND----5



round5=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlroundno_chosen")
time.sleep(1)
round5.click()
botton5_1=driver.find_element(By.XPATH, "//li[@data-option-array-index='5']")
time.sleep(1)
botton5_1.click()


insti_type=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstype_chosen")
time.sleep(1)
insti_type.click()
botton2=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[2]/div/div/div/ul/li[2]")
time.sleep(1)
botton2.click()



insti_name=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstitute_chosen")
time.sleep(1)
insti_name.click()
botton3=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[3]/div/div/div/ul/li[2]")
time.sleep(1)
botton3.click()


branch=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlBranch_chosen")
time.sleep(1)
branch.click()
botton4=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div/div/div/ul/li[2]")
time.sleep(1)
botton4.click()



category_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlSeattype_chosen")
time.sleep(1)
category_.click()
botton5=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[5]/div/div/div/ul/li[2]")
time.sleep(1)
botton5.click()




submit_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSubmit")
time.sleep(1)
submit_.click()

table5=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GridView1")
      

row5s = table5.find_elements(By.TAG_NAME, "tr")
header5s =table5.find_elements(By.TAG_NAME , "th")

title5s=[]
for i in header5s:
    title=i.text
    title5s.append(title)
df=pd.DataFrame(columns=title5s) 

data5 = []

for row in row5s[1:]:
    cells = row.find_elements(By.TAG_NAME, 'td')
    row_data5 = [cell.text for cell in cells]
    data5.append(row_data5)
    l=len(df)
    df.loc[l]=row_data5
print("success")
    
df.to_csv('Round_5.csv')


#### ROUND----6



round6=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlroundno_chosen")
time.sleep(1)
round6.click()
botton6_1=driver.find_element(By.XPATH, "//li[@data-option-array-index='6']")
time.sleep(1)
botton6_1.click()


insti_type=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstype_chosen")
time.sleep(1)
insti_type.click()
botton2=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[2]/div/div/div/ul/li[2]")
time.sleep(1)
botton2.click()



insti_name=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlInstitute_chosen")
time.sleep(1)
insti_name.click()
botton3=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[3]/div/div/div/ul/li[2]")
time.sleep(1)
botton3.click()


branch=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlBranch_chosen")
time.sleep(1)
branch.click()
botton4=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[4]/div/div/div/ul/li[2]")
time.sleep(1)
botton4.click()



category_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlSeattype_chosen")
time.sleep(1)
category_.click()
botton5=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/div[5]/div/div/div/ul/li[2]")
time.sleep(1)
botton5.click()




submit_=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSubmit")
time.sleep(1)
submit_.click()

table6=driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_GridView1")
      

row6s = table6.find_elements(By.TAG_NAME, "tr")
header6s =table6.find_elements(By.TAG_NAME , "th")

title6s=[]
for i in header6s:
    title=i.text
    title6s.append(title)
df=pd.DataFrame(columns=title6s) 

data6 = []

for row in row6s[1:]:
    cells = row.find_elements(By.TAG_NAME, 'td')
    row_data6 = [cell.text for cell in cells]
    data6.append(row_data6)
    l=len(df)
    df.loc[l]=row_data6
print("successfinally")
    
df.to_csv('Round_6.csv')
driver.quit()
