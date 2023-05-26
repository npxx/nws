from selenium import webdriver
from bs4 import BeautifulSoup
import requests
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

import csv

#headless browser stuff idk mann
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
#driver = webdriver.Chrome()
# to maximize the browser window
#driver.maximize_window()
#get method to launch the URL
driver.get("https://dailyepaper.in/times-of-india-epaper-pdf-download-2022/")
#timeout = 3
#try:
#    element_present = EC.presence_of_element_located((By.ID, 'main'))
#    WebDriverWait(driver, timeout).until(element_present)
#except TimeoutException:
#    print("Timed out waiting for page to load")
#finally:
#    print("Page loaded")
ps = driver.page_source
   
soup = BeautifulSoup(ps, 'html5lib')
   
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'class':'entry-content mh-clearfix'})

bruh=[]
u = table.findAll('p',attrs={'style':'text-align: center;'})
jj = u[1].find('span',attrs={'style':'font-size: 16px;'})
bruh.append(jj.text.split(': '))
gg=jj.find('a')
bruh.append(gg['href'])
print(bruh[1])

dd = requests.get(bruh[1])
jjj=BeautifulSoup(dd.content,'html5lib')
kkk=jjj.find('iframe',attrs={'id':'iframe'})
sss=kkk['src']

ss=requests.get(sss)
print('only writing left')

# Write content in pdf file
pdf = open("TOI_"+str(bruh[0][0])+".pdf", 'wb')
pdf.write(ss.content)
pdf.close()

print('Done lmao!')

