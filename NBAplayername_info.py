from selenium import  webdriver
from bs4 import BeautifulSoup

class Player():
	def __init__(self):
		self.name=""
		self.link=""

def get_player_list():

	driver=webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	url='http://www.nba.com/players'
	driver.get(url)



	soup=BeautifulSoup(driver.page_source,'lxml')

	div=soup.find('div',class_='small-12 columns')

	player_list=[]

	for a in div.find_all('a',class_='row playerList'):
		new_play=Player()
		new_play.name=a['title']
		new_play.link='http://www.nba.com'+a['href']
		player_list.append(new_play)

	for one_player in player_list:
		print one_player.name
		print one_player.link

	driver.quit
	return player_list

get_player_list()