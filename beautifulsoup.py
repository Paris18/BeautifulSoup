from bs4 import BeautifulSoup
import requests

i = 0
for item in ['java','python','go']: #its for more than on 1 languege output printing
	r = requests.get('http://www.tutorialspoint.com/%s/index.htm' %item) #geting resource for specified web page in object 'r'

	# for creating and writing into file'''
	with open("test2.html", "w") as f:
		f.write(r.content)

	# printing information from web page
	soup = BeautifulSoup(open("test2.html"),'html.parser')
	for ls in soup.find_all("ul", class_='left-menu'):
 		# ld=ls.find_all('a')
		print ls.get_text() #to print text field 

