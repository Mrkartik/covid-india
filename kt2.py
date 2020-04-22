"""
This is a Program which will fetch the data from original website of government.
Made by :
	Name:- Kartik Thakkar
	Email id:- kartik.thakkar@engineer.com
	C0ntribut0r:- Nikhil Gupta  (gnikhil@email.com) 
"""
# Import libraries##
from color import color
import requests
from bs4 import BeautifulSoup

#########################################################
#	2D Plotter by Nikhil Gupta<gnikhil@email.com>
#########################################################
def display(q):
	lorr = lambda a: a.rjust if a.isnumeric() else a.ljust #change rjust or ljust for justifying the place
	o=[0,0,0,0,0]
	for e in q: 
		for w in range(0,len(e)): o[w]=max(len(e[w]),o[w])
	for e in q:
		for c in range(0,len(e)):
			print(lorr(e[c])(o[c]," "),end="  ")#Use | instead of ' ' in end= for special effects
		print()
#################END#####################################
def rm(sr):                          #remove \n from data
	x=sr.replace("\n","")
	return x

url ='https://www.mohfw.gov.in/#site-advisories' #main url of government
response = requests.get(url)                     #get webpage
response.status_code														
response.content
soup = BeautifulSoup(response.content, 'html.parser')  #use html parser
kt2=soup.find('div',class_= "status-update")
kt3=""
#Loop to find out data from HTML Tags 
for row in kt2.find_all('h2'):
	kt3=str(row.text)[0:22]
	for col in row.find('span'):		
			kt3=kt3+str(color.Bold+str(color.Magenta+str(col)[7:]+color.End)+color.End)
kt =soup.find_all('tbody') 							 # find elements with tbody
kt=kt[0]														 
data=[]
str1=[]
data.append(["No","State","Confirmed Cases","Cured/Discharged","Death"])
for row in kt.find_all('tr'):
	for col in row.find_all('td'):
		str1.append(str(col.text))
	data.append(str1)
	str1=[]
dt1=data[33]
k=len(data)
i=32
del data[33:k]
print(color.Bold+(color.Blink + 'This data is taken from Website of Ministry of Health and Family Welfare. We have no control over data.' + color.End)+ color.End)
print(kt3)
data.append(["-","-"*26,"-"*15,"-"*15,"-"*5])
data.append([" ","Total",dt1[1][0:5],rm(dt1[2]),rm(dt1[3])])
data.append(["-","-"*26,"-"*15,"-"*15,"-"*5])
display(data)