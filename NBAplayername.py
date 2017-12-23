from selenium import  webdriver
from bs4 import BeautifulSoup

driver=webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url='http://www.nba.com/players'
driver.get(url)



soup=BeautifulSoup(driver.page_source,'lxml')

div=soup.find('div',class_='small-12 columns')

#print div
for a in div.find_all('span',class_='name-label'):
	print a.text

driver.quit