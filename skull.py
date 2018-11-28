character_donno='Null'
def meme():

		from PIL import Image

		a={1:'/home/dl116/Desktop/img jokes/image1.jpg',2:'/home/dl116/Desktop/img jokes/image2.jpg',3:'/home/dl116/Desktop/img jokes/image3.jpg',4:'/home/dl116/Desktop/img jokes/image4.jpg',5:'/home/dl116/Desktop/img jokes/image6.jpg',6:'/home/dl116/Desktop/img jokes/image7.jpg',7:'/home/dl116/Desktop/img jokes/image8.jpg',8:'/home/dl116/Desktop/img jokes/image9.jpg',9:'/home/dl116/Desktop/img jokes/image10.jpg'}
		print()
		import random
		c=a[random.randint(1,10)]

		with Image.open(c) as img:
		    img.show()
def google():
	import webbrowser
	query=input();
	url = "https://www.google.co.in/search?q=" + (str(query)) + "&oq=" + (
	str(query)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
	webbrowser.open(url)
def youtube():
	import webbrowser
	query=input();
	url = "https://www.youtube.com/search?q=" + (str(query)) + "&oq=" + (
	str(query)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
	webbrowser.open(url)					    
def repeat():
	print("\nOkay!",a,"what do you want me to do?")
	print("here's what i can do:")
	print("\ttell you a joke|take slefie|Play a Game|Calculator|Play a song|Play a video|")
	d=input("tell me!:")
	character_donno=d

def ladder():
	import random
	count=0
	def myroll():
		return random.randint(1,6)

	while(count<=100):
			n=input("press r to roll the dice")
			if(n=='r'):
				r=myroll()
				count=count+r
				print("you got ",r)
				print("new position is",count)

				if(count==8):
					count=37
					print("i got the ladder")
				elif(count==11):
					count=2
					print("sorry u got snake")
				elif(count==13):
					count=34
					print("i got the ladder")
				elif(count==25):
					count=4
					print("sorry u got snake")
				elif(count==40):
					count=68
					print("i got the ladder")
				elif(count==52):
					count=81
					print("i got the ladder")
				elif(count==65):
					count=46
					print("sorry u got snake")
				elif(count==76):
					count=97
					print("i got the ladder")
				elif(count==89):
					count=70
					print("sorry u got snake")
				elif(count==93):
					count=64
					print("sorry u got snake")
				elif(count==100):
					print("you won the game")

def rps():
	import random

	a={1:'rock',2:'paper',3:'scissor'}

	while True:
		p=input("your choice :")

		c=a[random.randint(1,3)]

		print("you chose:",p,"computer choice:",c)

		if(p==c):
			print("draw")
		elif(p=="rock" and c=="paper"):
			print("you lose")
		elif(p=="rock" and c=="scissor"):
			print("you win")
		elif(p=="paper" and c=="rock"):
			print("you win")
		elif(p=="paper" and c=="scissor"):
			print("you win")
		elif(p=="scissor" and c=="rock"):
			print("you lose")
		elif(p=="scissor" and c=="paper"):
			print("$you win$")

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

print("\t\t*****Hi there! I'm Skully*******")
print("\nHow can i help?")
sleep(2)
print("\nmm....looks like you're a new user!")
sleep(3)
print("\ncan you help me in knowing you better?")
a=input("\nWhat's your name?")
print(a,"...that's a nice name")
b=input("\nyour age?")
c=input("\nyour gender?")
repeat()	
if(character_donno=="tell me a joke"):
	print("\ti have got plenty of them! ;)")
	meme()
	e=input("\n Do you want more?")
	if(e=='Y' or e=='y' or e=='Yes' or e=='yes' or e=='ya' or e=='yup'):
		print("\nhmmm...thats! good!")
		sleep(2)
		meme()
	else:
		print("No problem! you can try other things too!")	
elif(character_donno=="tell me a joke"):
elif(character_donno=="tell me a joke"):
elif(character_donno=="tell me a joke"):
elif(character_donno=="tell me a joke"):
elif(character_donno=="tell me a joke"):	
