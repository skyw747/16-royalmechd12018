def heyskully():	
	import speech_recognition as sr
	r=sr.Recognizer()
	with sr.Microphone() as mc:
		r.adjust_for_ambient_noise(mc,duration=5)
		r.dynamic_energy_thershold = True
		print('say!!!')
		audio = r.listen(mc)
	try:
		heyskully.u=r.recognize_google(audio)
	except sr.UnknownValueError:
		print("I didn't get that!")
	except sr. RequestError as e:
		print('could connect to google: {0}'.format(e))	

def meme():

		from PIL import Image

		a={1:'/home/dl116/Desktop/img jokes/image1.jpg',2:'/home/dl116/Desktop/img jokes/image2.jpg',3:'/home/dl116/Desktop/img jokes/image3.jpg',4:'/home/dl116/Desktop/img jokes/image4.jpg',5:'/home/dl116/Desktop/img jokes/image6.jpg',6:'/home/dl116/Desktop/img jokes/image7.jpg',7:'/home/dl116/Desktop/img jokes/image8.jpg',8:'/home/dl116/Desktop/img jokes/image9.jpg',9:'/home/dl116/Desktop/img jokes/image10.jpg'}

		import random
		c=a[random.randint(1,10)]

		with Image.open(c) as img:
		    img.show()
def google():
	import webbrowser
	print("lemme ask google...")
	sleep(1)
	query=input("what you wanna know?");
	url = "https://www.google.co.in/search?q=" + (str(query)) + "&oq=" + (
	str(query)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
	webbrowser.open(url)
def youtube():
	import webbrowser
	query=input(" what do you wanna see?");
	url = "https://www.youtube.com/search?q=" + (str(query)) + "&oq=" + (
	str(query)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
	webbrowser.open(url)					    
def repeat():
	print("\nOkay!",a,"what do you want me to do?")
	print("here's what i can do:")
	print("\t|tell you a joke| \n\t|take slefie| \n\t|Play a Game| \n\t|Calculator| \n\t|Play a video| \n\t|search for anything |")

def calcii():
	def add(x, y):
	   return x + y

	def subtract(x, y):
	   return x - y

	def multiply(x, y):
	   return x * y

	def divide(x, y):
	   return x / y

	print("This is what i have learnt so far:")
	print("Addition")
	print("Subtraction")
	print("Multiplication")
	print("Division")

	choice = input("what should i do?")

	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))

	if choice == 'Addition':
	   print(num1,"+",num2,"=", add(num1,num2))

	elif choice == 'Subtraction':
	   print(num1,"-",num2,"=", subtract(num1,num2))

	elif choice == 'Multiplication':
	   print(num1,"*",num2,"=", multiply(num1,num2))

	elif choice == 'Division':
	   print(num1,"/",num2,"=", divide(num1,num2))
	else:
	   print("I don't know to do that!")

	

def ladder():
	import random
	 
	count=0

	def myroll():
		return random.randint(1,6)

	while(count<=100):
		print(a,"!")
		n=input('press r to roll the die:')
		if(n=='r'):	
			r=myroll()
			if(r==6):
				print('\t\t**yoohoo its a six!!**\t\t')
			count=count+r
			print('u got:',r)
			print('your new position:',count)
			if(count==8):
				count=37
				print('\t\t**gotcha ladder!**\t\t')
			elif(count==11):
				count=2
				print('\t\t**hiss! snaaakee!!!**\t\t')
				print('you are at:',count)
			elif(count==13):
				count=34
				print('\t\t**gotcha ladder!**\t\t')
				print('you are at:',count)
			elif(count==25):
				count=4
				print('\t\t**hiss! snaaakee!!!**\t\t')
				print('you are at:',count)     
			elif(count==38):
				count=9
				print('\t\t**hiss! snaaakee!!!**\t\t')
				print('you are at:',count)
			elif(count==40):
				count=68
				print('\t\t**gotcha ladder!**\t\t')
				print('you are at:',count)
			elif(count==52):
				count=81
				print('\t\t**gotcha ladder!**\t\t')
				print('you are at:',count)
			elif(count==65):
				count=46
				print('\t\t**hiss! snaaakee!!!**\t\t')
				print('you are at:',count)
			elif(count==93):
				count=64
				print('\t\t**hiss! snaaakee!!!**\t\t')
				print('you are at:',count)
			elif(count==89):
				count=70
				print('\t\t**hiss! snaaakee!!!**\t\t')
				print('you are at:',count)
			elif(count==76):
				count=97
				print('\t\t**gotcha ladder!**\t\t')
				print('you are at:',count)
			elif(count==100):
				print('\t\t\t***** You Won!! ',a,'!  *****\t\t\t')
				break
			elif(count>100):
				count=count-r
				print('thats more then hundred!')	
		else:
			print('wrong key!')
			exit()		                               



def rps():
	import random
	count=0
	cscore=0
	a={1:'rock',2:'paper',3:'scissor'}

	while True:
		print(a,"!")
		p=input('enter your choice:')

		c=a[random.randint(1,3)]

		print(a,"! chose:",p,"\nSkully chose:",c)

		if(p==c):
			print('\t\t   **Draw!**  ')
		elif(p=='rock' and c=='paper'):
			print('\t\t ## you lose! ##')
			cscore=cscore+1
		elif(p=='rock' and c=='scissor'):
			print('\t\t ## Winner winner chicken Dinner! ## ')
			count=count+1
		elif(p=='paper' and c=='rock'):
			print('\t\t## Winner winner chicken Dinner! ##')
			count=count+1
		elif(p=='paper' and c=='scissor'):
			print('\t\t ## you lose! ## ')
			cscore=cscore+1
		elif(p=='scissor' and c=='rock'):
			print('\t\t ## you lose! ## ')
			cscore=cscore+1
		elif(p=='scissor' and c=='paper'):
			print('\t\t ## Winner winner chicken Dinner! ## ')
			count=count+1
		else:
			print('\n\t Bored?')
			print("\t\t## Scores  ##")
			print(a,": ",count,"Skully: ",cscore)
			if(count>cscore):
				print("you nailed it!",)
			elif(count<cscore):
				print("Skully won!")
			else:
				print('its draw!')		
			exit()						
			
def selfie():
	import os
	from time import sleep

	def mymail():
		return

	def takesnap():
		os.system("fswebcam -F 4 /home/dl114/Rahulroy/img/tmp.jpg")
		return

	for i in range(10):
		takesnap()
		mymail()
		sleep(5)


from time import sleep
print('\t\t\t       .ed"""" """$$$$be.')
print('\t\t\t     -"           ^""**$$$e.')
print('\t\t\t   ."                   \'$$$c')
print('\t\t\t  /                      "4$$b')
print('\t\t\t d  3                      $$$$')
print('\t\t\t $  *                   .$$$$$$')
print('\t\t\t.$  ^c           $$$$$e$$$$$$$$.')
print('\t\t\td$L  4.         4$$$$$$$$$$$$$$b')
print('\t\t\t$$$$b ^ceeeee.  4$$ECL.F*$$$$$$$')
print('\t\t\t$$$$P d$$$$F $ $$$$$$$$$- $$$$$$')
print('\t\t\t3$$$F "$$$$b   $"$$$$$$$  $$$$*"')
print('\t\t\t $$P"  "$$b   .$ $$$$$...e$$')
print('\t\t\t  *c    ..    $$ 3$$$$$$$$$$eF')
print('\t\t\t    %ce""    $$$  $$$$$$$$$$*')
print('\t\t\t     *$e.    *** d$$$$$"L$$')
print('\t\t\t      $$$      4J$$$$$% $$$')
print('\t\t\t     $"\'$=e....$*$$**$cz$$"')
print('\t\t\t     $  *=%4.$ L L$ P3$$$F')
print('\t\t\t     $   "%*ebJLzb$e$$$$$b')
print('\t\t\t      %..      4$$$$$$$$$$')
print('\t\t\t       $$$e   z$$$$$$$$$$')
print('\t\t\t        "*$c  "$$$$$$$P"')
print('\t\t\t          """*$$$$$$$"')

print("\t","-"*60)
print("\t\t||*****Hi there! I'm Skully*******\t||")
print("\t","-"*60)
sleep(1)
print("\n","-"*16)
print("How can i help?")
print("-"*16)
sleep(1)
print("\n","-"*38)
print("can you help me in knowing you better?")
print("-"*38)
sleep(1)
print("\n","-"*18)
a=input("What's your name?")
print("-"*18)
sleep(1)
print("\n","-"*30)
print(a,"...that's a nice name")
print("-"*30)
'''b=input("\nyour age?")
c=input("\nyour gender?")'''
repeat()
d=input("tell me!:")
#heyskully()
#print("you told:",heyskully.u)
#heyskully.u=d
	
if(d=="tell me a joke"):
	print("\ti have got plenty of them! ;)")
	meme()
	e=input("\n Do you want more?")
	if(e=='Y' or e=='y' or e=='Yes' or e=='yes' or e=='ya' or e=='yup' or e=='yea'):
		print("\nhmmm...thats! good!")
		sleep(2)
		meme()
		break
	else:
		print("\n","-"*42)
		print("No problem! you can try other things too!")
		print("-"*42)
		break

elif(d=="take a selfie" or d=="selfie" or d=="click a pic" or d=="picture" or d=="photo" or d=="take"):
	selfie()

elif(d=="play a game"):
	print("here's what i know to play:")
	print("\tSnake and ladder \n\t rock paper scissor \n\t tic tac toe")
	print(" so...")
	sleep(1)
	l=input("what did you plan to play?")
	if(l=="snake and ladder" or l=="Snake & ladder" or l=="snake" or l=="ladder" ):
		sleep(1)
		print("you see! i'm gonna win! ;)")  
		ladder()
	elif (l=="rock paper scissor" or l=="rps" or l=="Rock" or l=="paper" or l=="scissor"):
		print("i am pro at this game!")
		rps()
			

elif(d=="search for anything"):
	sleep(1)
	google()
elif(d=="calculate"):
	print("i am a maths freak! you know!")
	sleep(1)
	calcii()
elif(d=="play a video"):
	print("i can singer better than justin bieber but i will let youtube do the work!")
	sleep(1)
	youtube()