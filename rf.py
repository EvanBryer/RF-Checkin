import time
from datetime import date
import re

day = date.today()

#Clean newline characters from inputs
def clean(s):
	return re.sub("\n","",s)


#Initialize the database and load known ids
def init():
	database = open('./data/base.txt','r').readlines()
	try:
		today = open(f'./data/{day}.txt','r')
	except:
		today = open(f'./data/{day}.txt','w')
	names = []
	ids = []
	for l in database:
		s = l.split("\t")
		ids.append(clean(s[0]))
		names.append(clean(s[1]))
	db = {ids[i]: names[i] for i in range(len(ids))}
	return db

#Init the database
db = init()

#Main function. Gets name, checks if its known, if not adds them to the knowledge base
def doRF(ID):
	k=db.keys()
	if ID not in db.keys():
		name = input("New ID detected. Enter your name: ")
		db[ID] = name
		database = open('./data/base.txt','a')
		database.write(f"{ID}\t{name}\n")
	print(f"{db[ID]}, you have been checked in!")
	name = db[ID]
	names = open(f'./data/{day}.txt','r').read()
	if name not in names:
		sign = open(f'./data/{day}.txt','a')
		sign.write(f"{name}\t{time.time()}\t\n")
	#else:
	#	sign = open(f'./data/{day}.txt','w')
	#	sign.write(f"{name}\t{time.time()}\n")
	time.sleep(2)

#Used to clear the screan after inputs
def clear():
	print("\n"*100)


#Main loop.
while True:
	clear()
	print("Garnet Squad RFID Scanner")
	print("Please Scan your RFID card now.")
	ID = input()
	doRF(clean(ID))
