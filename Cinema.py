#Manage All Movie
class Movie:
	Movie_list={"Avengers":[],"Thor":[],"Dr_Strange":[]}
	@classmethod
	def showList(cls):
		print(cls.Movie_list.keys())
		print("영화를 선택해주세요 :",end=' ')
	@classmethod
	def timeList(cls, mv_choice):
		print(cls.Movie_list[mv_choice])

#Set each movie
class EachMovie(Movie):
	def __init__(self,name, room, time):
		self.room=room
		self.time=time
		self.Movie_room=[[" ",1,2,3,4,5],["A",0,0,0,0,0],["B",0,0,0,0,0],["C",0,0,0,0,0],["D",0,0,0,0,0],["E",0,0,0,0,0]]
		Movie.Movie_list[name].append(time)
	
	def reserve(self, x, y, num):
		check=0
		#Already reserved
		for i in range(0,num): 
			if self.Movie_room[x][y+i]==1:
				print("이미 예약된 좌석입니다.")
				break
			elif i==num-1:
					check=1
		#Not reserved
		if check==1:
			for i in range(0,num):
				self.Movie_room[x][y+i]=1
	#Print Seat
	def showRoom(self):
		print(self.Movie_room)
#Manage All Audience
class Person:
	income=0
	num=0
	@classmethod
	def show_income(cls):
		print(cls.income)
	@classmethod
	def show_num(cls):
		print(cls.num)
#Manage each group	
class Group(Person):
	def __init__(self,child,teen,adult):
		self.child_count=child
		self.teen_count=teen
		self.adult_count=adult
		self.num=child+teen+adult
		self.price=5000 * child+ 7000 * teen + 8000 * adult
	def total_price(self):
		Person.income+=self.price
		return self.price
	def group_num(self):
		Person.num+=self.num
		return self.num

def Main_menu():
	text=["Menu","1.Reserve","2.Show Time","3.Total income","4.Exit"]
	print("-"*40)
	print(f"{text[0]:^40}")
	print(f"{text[1]:^40}")
	print(f"{text[2]:^40}")
	print(f"{text[3]:^40}")
	print(f"{text[4]:^40}")
	choice=input()
	if choice=="1":
		Reserve_menu()
	elif choice=="2":
		Time_menu()
	elif choice=="3":
		Income_menu()
	elif choice=="4":
		Exit()
	else:
		print("다시 입력해주세요")
		Main_menu()

def Reserve_menu():
	Movie.showList()
	mv_choice=input() #name
	Movie.timeList(mv_choice) 
	time_choice=input("시간을 선택해주세요") #time
	
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
	

def Income_menu():
	pass
def Exit():
	pass
	
fuc={'A1':[]}	
A1=EachMovie("Avengers",1,"08:00")
A2=EachMovie("Avengers",1,"12:00")
A3=EachMovie("Avengers",1,"18:00")

B1=EachMovie("Thor",2,"09:00")
B2=EachMovie("Thor",2,"13:00")

Main_menu()
