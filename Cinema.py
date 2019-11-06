# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#Manage All Movie
import time
import os

def WhichMovie(mv_name,time):
	for i in Movie.Movie_info[mv_name]:
		if i[0]==time:
			return i[1]

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

class Movie:
	income=0
	num=0
	Movie_info={"Avengers":[],"Thor":[],"Dr_Strange":[]}
	client_log=[]
	@classmethod
	def show_income(cls):
		print(cls.income)
	@classmethod
	def show_num(cls):
		print(cls.num)
	@classmethod
	def showInfo(cls):
		print(cls.Movie_info)
	@classmethod
	def showList(cls):
		print(cls.Movie_info.keys())
		print("영화를 선택해주세요 :",end=' ')
	@classmethod
	def timeList(cls, mv_choice):
		print(cls.Movie_info[mv_choice])

#Set each movie
class EachMovie(Movie):
	def __init__(self,name, room, time,mv_ID):
		self.room=room
		self.time=time
		self.ID=mv_ID
		self.Movie_room=[[" ","01","02","03","04","05"],["A",0,0,0,0,0],["B",0,0,0,0,0],["C",0,0,0,0,0],["D",0,0,0,0,0],["E",0,0,0,0,0]]
		Movie.Movie_info[name].append([time,mv_ID])
	
	#Print Seat
	def showRoom(self):
		for i in self.Movie_room:
			for j in i:
				print(j, end=' ')
			print("\n")
	
	def Reserve(self):
		reserve_count=0
		client_num=input("인원을 입력해주세요. 아이/청소년/어른")
		a=client_num.split("/")
		total_member=int(a[0])+int(a[1])+int(a[2])
		total_price=5000*int(a[0])+7000*int(a[1])+8000*int(a[2])
		if total_member>self.LeftSeat():
			print("잔여좌석이 없습니다. 다른 영화를 예약해주세요")
			time.sleep(10)
		self.showRoom()
		while reserve_count<total_member :
			temp=input("좌석을 선택해주세요(예시:A01):")
			tmp=temp.split("0")
			for i in self.Movie_room:
				if i[0]==(tmp[0]):
					if i[int(tmp[1])]==0:
						i[int(tmp[1])]='T'
						reserve_count+=1
						break
					else :
						print("이미 찬 자리입니다. 다른자리를 선택해주세요")  ## 리스트 범위 밖이면 다시 출력하도록
						break
		print("요금은 총 %d입니다. 결제하시겠습니까(y/n)"%total_price)
		payment=input()
		if payment=="y":
			self.PayComplete()
			Movie.client_log.append([self.ID,client_num,total_price])
			Movie.income+=total_price
		else :
			self.PayFail()
		MainMenu()

	def LeftSeat(self):
		self.left=0
		for i in self.Movie_room:
			self.left+=i.count(0)
		return self.left
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


#ok
def Time_menu():
	Movie.showList()
	mv_choice=input()
	Movie.timeList(mv_choice)
	onemore=input("다른 영화의 시간표를 보시겠습니까? (y/n)")
	if onemore=="y":
		Time_menu()
	else:
		Main_menu()
	
	
mv_1=EachMovie("Avengers",1,"08:00",1)
mv_2=EachMovie("Avengers",1,"12:00",2)
mv_3=EachMovie("Avengers",1,"18:00",3)

mv_4=EachMovie("Thor",2,"09:00",4)
mv_5=EachMovie("Thor",2,"13:00",5)
Movie.showInfo()
print(WhichMovie("Avengers","08:00"))

def MainMenu():
	text=["Menu","1.Reserve","2.Show Time","3.Total income","4.Exit"]
	print("-"*40)
	print(f"{text[0]:^40}")
	print(f"{text[1]:^40}")
	print(f"{text[2]:^40}")
	print(f"{text[3]:^40}")
	print(f"{text[4]:^40}")
	choice=input()
	if choice=="1":
		Movie.showList()
		mv_choice=input("영화를 선택해주세요")
		Movie.timeList(mv_choice) 
		time_choice=input("시간을 선택해주세요") #time
		mv_reserve(WhichMovie(mv_choice,time_choice)) #Print Seat 
	
	elif choice=="2":
		Time_menu()
	
	elif choice=="3":
		os.system("clear")
		Movie.show_income()
		time.sleep(5)
		MainMenu()
	elif choice=="4":
		pass
	else:
		print("다시 입력해주세요")
		MainMenu()

MainMenu()
