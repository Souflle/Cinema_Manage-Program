import time
import os

#Finde Movie ID 
def WhichMovie(mv_name,time):
	for i in Movie.Movie_info[mv_name]:
		if i[0]==time:
			return i[1]
	return 0
	
#Execute class function corresponding with Movie ID
def mv_reserve(Movie_ID):
	if Movie_ID==1:
		mv_1.Reserve()
	elif Movie_ID==2:
		mv_2.Reserve()
	elif Movie_ID==3:
		mv_3.Reserve()
	elif Movie_ID==4:
		mv_4.Reserve()
	elif Movie_ID==5:
		mv_5.Reserve()
	elif Movie_ID==6:
		mv_6.Reserve()
	elif Movie_ID==7:
		mv_7.Reserve()
	elif Movie_ID==8:
		mv_8.Reserve()
	elif Movie_ID==9:
		mv_9.Reserve()	
#Manage all Cinema
class Movie:
	income=0
	num=0
	Movie_info={"Avengers":[],"Thor":[],"Dr_Strange":[]}
	client_log=[]
	@classmethod
	def show_Income(cls):
		print(cls.income)
	@classmethod
	def show_MovieList(cls):
		print(cls.Movie_info.keys())
		print("Select Movie :",end=' ')
	@classmethod
	def show_TimeList(cls, mv):
		print("TimeList:")
		for i in Movie.Movie_info[mv]:
			print(i[0],end='	')
		print("")

#Set each movie
class EachMovie(Movie):
	def __init__(self,name, room, time,mv_ID):
		self.room=room
		self.time=time
		self.ID=mv_ID
		self.Movie_room=[[" ","01","02","03","04","05"],["A",0,0,0,0,0],["B",0,0,0,0,0],["C",0,0,0,0,0],["D",0,0,0,0,0],["E",0,0,0,0,0]]
		Movie.Movie_info[name].append([time,mv_ID])
	
	#Print Seat
	def show_Room(self):
		for i in self.Movie_room:
			for j in i:
				print(j, end=' ')
			print("\n")
	def Reserve(self):
		reserve_count=0
		member_flag=0
		while member_flag==0:
			client_num=input("Please enter the number of people(Child/Teen/Adult)")
			a=client_num.split("/")
			if member_Check(a)==1:
				member_flag=1
				total_member=int(a[0])+int(a[1])+int(a[2])
				total_price=5000*int(a[0])+7000*int(a[1])+8000*int(a[2])
		if total_member>self.Count_LeftSeat():
			print("There are no seats left. Please Book another movie")
			time.sleep(3)
			Main_Menu()
		self.show_Room()
		while reserve_count<total_member :
			temp=input("Please select a seat(ex:A01):")
			tmp=temp.split("0")
			for i in self.Movie_room:
				if (room_Check(tmp)==1):
					if i[0]==(tmp[0]):
						if i[int(tmp[1])]==0:
							i[int(tmp[1])]='T'
							reserve_count+=1
							print("Reserved")
							break
						else :
							print("It's already Booked. Please select another seat")  
							break
				else:
					break
		print("The total is %d won. Would you like to pay?(y/n)"%total_price)
		payment=input()
		if payment=="y":
			self.PayComplete()
			Movie.client_log.append([self.ID,client_num,total_price])
			Movie.income+=total_price
		else :
			self.PayFail()
		Main_Menu()

	def Count_LeftSeat(self):
		self.Left_Seat=0
		for i in self.Movie_room:
			self.Left_Seat+=i.count(0)
		return self.Left_Seat
	def PayComplete(self):
		for i in range(1,6):
			for j in range(1,6):
				if self.Movie_room[i][j]=='T':
					self.Movie_room[i][j]=1
	def PayFail(self):
			for i in range(1,6):
				for j in range(1,6):
					if self.Movie_room[i][j]=='T':
						self.Movie_room[i][j]=0
def Main_Menu():
	os.system("clear")
	name_flag=0
	ID_flag=0
	text=["Menu","1.Reserve","2.Show Time","3.Total income","4.Exit"]
	print("-"*40)
	print(f"{text[0]:^40}")
	print(f"{text[1]:^40}")
	print(f"{text[2]:^40}")
	print(f"{text[3]:^40}")
	print(f"{text[4]:^40}")
	choice=input()
	if choice=="1":
		os.system("clear")
		Movie.show_MovieList()
		while name_flag==0:
			mv_choice=input("Please select a movie : ")
			if name_check(mv_choice)==1:
				name_flag=1
		Movie.show_TimeList(mv_choice)
		while ID_flag==0:
			time_choice=input("Please select a time : ")
			if WhichMovie(mv_choice, time_choice)!=0:
				ID_flag=1
				mv_reserve(WhichMovie(mv_choice,time_choice)) 
			else :
				print("Please enter the time again")
	elif choice=="2":
		Time_Menu()
	elif choice=="3":
		os.system("clear")
		Movie.show_Income()
		time.sleep(3)
		Main_Menu()
	elif choice=="4":
		print("Exit")
		pass
	else:
		print("Please enter again")
		Main_Menu()

def Time_Menu():
	name_flag=0
	os.system("clear")
	Movie.show_MovieList()
	while name_flag==0:
			mv_choice=input("Please select a movie : ")
			if name_check(mv_choice)==1:
				name_flag=1
	Movie.show_TimeList(mv_choice)
	onemore=input("Would you like to see another movie's timetable? (y/n)")
	if onemore=="y":
		Time_Menu()
	else:
		Main_Menu()

#Exception Processing function
def name_check(mv_choice):
	try:
		Movie.Movie_info[mv_choice]
	except KeyError :
		print("You have entered an incorrect movie title. Please enter again")
		return 0
	else: 
		return 1
def room_Check(tmp):
	try:
		if 0<int(tmp[1]) & int(tmp[1])<6:
			return 1
	except IndexError:
		print ("Please enter in the correct format")
		return 0
def member_Check(a):
	try :
		total_member=int(a[0])+int(a[1])+int(a[2])
		return 1
	except ValueError:
		print("Please enter in the correct format")
		return 0
	
#Set Each Movie
mv_1=EachMovie("Avengers",1,"08:00",1)
mv_2=EachMovie("Avengers",1,"12:00",2)
mv_3=EachMovie("Avengers",1,"18:00",3)
mv_4=EachMovie("Thor",2,"09:00",4)
mv_5=EachMovie("Thor",2,"13:00",5)
mv_6=EachMovie("Dr_Strange",3,"09:00",6)
mv_7=EachMovie("Dr_Strange",3,"12:00",7)
mv_8=EachMovie("Dr_Strange",3,"16:00",8)
mv_9=EachMovie("Dr_Strange",3,"20:00",9)
	
Main_Menu()
