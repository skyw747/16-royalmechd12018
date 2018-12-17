'''def legends():
	from PIL import Image
		a={1:"#location",2:"#location",3:"#location",4:"#location"}
		for i in range(1,5):
			c=a[i]
			with Image.open(c) as img:
				img.show()'''
def tic():
	import random
	from time import sleep
	from os import system

	a=[1,2,3,4,5,6,7,8,9]
	def printboard():
		print('_',a[0],'_|_',a[1],'_|_',a[2],'_')
		print('_',a[3],'_|_',a[4],'_|_',a[5],'_')
		print(' ',a[6],' | ',a[7],' | ',a[8],' ')

	def possibilities():
		l = []
		for i in a:
			if (i!='𝐗' and i != '𝐎'):
				l.append(i)
		return l

	def compTurn():
		temp = possibilities()
		k = random.choice(temp)
		return k

	pl1=True
	while True:
		print("\n")

		printboard()
		if pl1:
			p=int(input("\nChoose your place:"))
			if(p in a):
				print("you  chose:",p)
				a[p-1]='𝐗'
				pl1 = not pl1
		else:
			w = compTurn()
			print("sᴋᴜʟʟʏ chose:",w)
			sleep(3)
			a[int(w)-1]='𝐎'
			pl1 = not pl1

		for i in (0,3,6):
			if(a[i]==a[i+1] and a[i]==a[i+2]):
				printboard()
				if(a[i]=='𝐗'):
					print("\t\t\tʏᴏᴜ ɴᴀɪʟᴇᴅ ɪᴛ!🎖")
					exit()
				else:
					print("\t\t\tsᴋᴜʟʟʏ ᴡᴏɴ!🎖")
					exit()

		for i in range(3):
			if(a[i]==a[i+3] and a[i]==a[i+6]):
				printboard()
				if(a[i]=='𝐗'):
					print("\t\t\tʏᴏᴜ ɴᴀɪʟᴇᴅ ɪᴛ!🎖")
					exit()
				else:
					print("\t\t\tsᴋᴜʟʟʏ ᴡᴏɴ!🎖")
					exit()

		if(a[0]==a[4] and a[0]==a[8]): 				
			printboard()
			if(a[0]=='𝐗'):
					print("\t\t\tʏᴏᴜ ɴᴀɪʟᴇᴅ ɪᴛ!🎖")
					exit()
			else:
					print("\t\t\tsᴋᴜʟʟʏ ᴡᴏɴ!🎖")
					exit()

		elif(a[2]==a[4] and a[2]==a[6]): 
			printboard()
			if(a[2]=='𝐗'):
					print("\t\t\tʏᴏᴜ ɴᴀɪʟᴇᴅ ɪᴛ!🎖")
					exit()
			else:
					print("\t\t\tsᴋᴜʟʟʏ ᴡᴏɴ!🎖")
					exit()
		t = possibilities()
		if len(t) == 0:
			printboard()
			print("It's a tie ...")
			exit()

def read():
	from gtts import gTTS 
	import os
	global mytext
	mytext = "i am skaalley created by thennavan siddharth vishnu thaasin"
	language = 'en'
	myobj = gTTS(text=mytext, lang=language, slow=False) 
	myobj.save("welcome.mp3") 
	os.system("welcome.mp3")

def shopping():
	import webbrowser
	query=input("what you wanna buy?");
	url = "https://www.ebay.in"
	webbrowser.open(url)




def name():
	global c
	a={1:"ᴛʜᴀᴛ's ᴛʜᴇ ᴡᴏʀsᴛ ɴᴀᴍᴇ ɪ ʜᴀᴠᴇ ᴇᴠᴇʀ ʜᴇᴀʀᴅ!👿",2:"ɪ ᴛʜɪɴᴋ ʏᴏᴜʀ ᴀʀᴇ ʀᴏᴍᴀɴᴛɪᴄ ᴘᴇʀsᴏɴ😍",3:"ᴛʜᴀᴛ's ᴀ ʙᴇᴀᴜᴛɪғᴜʟ ɴᴀᴍᴇ😘",4:"ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ᴛᴏ ᴛʏᴘᴇ ᴍʏ ɴᴀᴍᴇ😖",5:"ᴡʜᴏ ᴛʜᴇ ʜᴇʟʟ ᴀʀᴇ ʏᴏᴜ👿",6:"ᴛʜᴀᴛ's ᴀ ғᴜɴɴʏ ɴᴀᴍᴇ😂",7:"ᴛʜᴀᴛ's ᴍʏ ғʀɪᴇɴᴅ's ɴᴀᴍᴇ😜",8:"ᴛʜᴀᴛ's ᴀ sᴡᴇᴇᴛ ɴᴀᴍᴇ😋",9:"ʏᴏᴜ ᴡɪʟʟ ᴅɪᴇ sɪɴɢʟᴇ!😭",10:"ɢᴏ! ɢᴇᴛ ᴀ ʙᴇᴛᴛᴇʀ ɴᴀᴍᴇ!🤦"}
	import random
	c=a[random.randint(1,10)]
def maps(): 
	import webbrowser
	print("\n","-"*42)
	query=input("where do you wanna go?")
	print("-"*42)
	url = "https://www.google.com/maps/@13.1228551,77.6593282,15zsearch?q=" + (str(query)) + "&oq=" + (
	str(query)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
	webbrowser.open(url)
def heyskully():
	import speech_recognition as sr
	global x
		
	r=sr.Recognizer()
	with sr.Microphone() as mc:
		r.adjust_for_ambient_noise(mc,duration=5)
		r.dynamic_energy_thershold = True
		print('sᴀʏ!!!')
		audio = r.listen(mc)     
	try:
		x=r.recognize_google(audio)
	except sr.UnknownValueError:
		print("ɪ ᴅɪᴅɴ'ᴛ ɢᴇᴛ ᴛʜᴀᴛ!")
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
	print("\n","-"*42)
	print("ʟᴇᴍᴍᴇ ᴀsᴋ ɢᴏᴏɢʟᴇ...")
	print("-"*42)
	sleep(1)
	query=input("ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴɴᴀ ᴋɴᴏᴡ?");
	url = "https://www.google.co.in/search?q=" + (str(query)) + "&oq=" + (
	str(query)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
	webbrowser.open(url)
def youtube():
	import webbrowser
	query=input("ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴɴᴀ sᴇᴇ?");
	url = "https://www.youtube.com/search?q=" + (str(query)) + "&oq=" + (
	str(query)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
	webbrowser.open(url)					    
def repeat():
	print("\n","-"*42)
	print("ᴏᴋᴀʏ!",a,"ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ?")
	print("-"*42)
	print("ʜᴇʀᴇ's ᴡʜᴀᴛ ɪ ᴄᴀɴ ᴅᴏ:")
	print("\t|ᴛᴇʟʟ ʏᴏᴜ ᴀ ᴊᴏᴋᴇ      | \n\t|ᴛᴀᴋᴇ sʟᴇғɪᴇ          |\n\t|ᴘʟᴀʏ ᴀ ɢᴀᴍᴇ          | \n\t|ᴄᴀʟᴄᴜʟᴀᴛᴏʀ           |\n\t|ᴘʟᴀʏ ᴀ ᴠɪᴅᴇᴏ         |\n\t|sᴇᴀʀᴄʜ ғᴏʀ ᴀɴʏᴛʜɪɴɢ  | \n\t|ᴍᴀᴘs                 |\n\t|sʜᴏᴘᴘɪɴɢ             |")

def calcii():
	def add(x, y):
	   return x + y

	def subtract(x, y):
	   return x - y

	def multiply(x, y):
	   return x * y

	def divide(x, y):
	   return x / y

	print("ᴛʜɪs ɪs ᴡʜᴀᴛ ɪ ʜᴀᴠᴇ ʟᴇᴀʀɴᴛ sᴏ ғᴀʀ:")
	print("ᴀᴅᴅɪᴛɪᴏɴ")
	print("sᴜʙᴛʀᴀᴄᴛɪᴏɴ")
	print("ᴍᴜʟᴛɪᴘʟɪᴄᴀᴛɪᴏɴ")
	print("ᴅɪᴠɪsɪᴏɴ")

	choice = input("ᴡʜᴀᴛ sʜᴏᴜʟᴅ ɪ ᴅᴏ?")


	num1 = int(input("ᴇɴᴛᴇʀ ғɪʀsᴛ ɴᴜᴍʙᴇʀ: "))
	num2 = int(input("ᴇɴᴛᴇʀ sᴇᴄᴏɴᴅ ɴᴜᴍʙᴇʀ: "))

	if choice == 'Addition':
	   print(num1,"+",num2,"=", add(num1,num2))

	elif choice == 'Subtraction':
	   print(num1,"-",num2,"=", subtract(num1,num2))

	elif choice == 'Multiplication':
	   print(num1,"*",num2,"=", multiply(num1,num2))

	elif choice == 'Division':
	   print(num1,"/",num2,"=", divide(num1,num2))
	else:
		print("\n","-"*42)
		print("ɪ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ!")
		print("-"*42)

	

def ladder():
	import random
	print("\n\t\t\t*******𝙇𝙀𝙏'𝙎 𝙂𝙊!!!*******\n")
	 
	count=0

	def myroll():
		return random.randint(1,6)

	while(count<=100):
		print(a,"!")
		n=input('ᴘʀᴇss ʀ ᴛᴏ ʀᴏʟʟ ᴛʜᴇ ᴅɪᴇ 🎲:')
		if(n=='r'):	
			r=myroll()
			if(r==6):
				print('\t\t**ʏᴏᴏʜᴏᴏ ɪᴛs ᴀ sɪx!!**\t\t')
			count=count+r
			print('ᴜ ɢᴏᴛ:',r)
			print('ʏᴏᴜʀ ɴᴇᴡ ᴘᴏsɪᴛɪᴏɴ:',count)
			if(count==8):
				count=37
				print('\t\t**ɢᴏᴛᴄʜᴀ ʟᴀᴅᴅᴇʀ!**🛤\t\t')
			elif(count==11):
				count=2
				print('\t\t**ʜɪss! sɴᴀᴀᴀᴋᴇᴇ!!!**🐍\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)
			elif(count==13):
				count=34
				print('\t\t**ɢᴏᴛᴄʜᴀ ʟᴀᴅᴅᴇʀ!**🛤\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)
			elif(count==25):
				count=4
				print('\t\t**ʜɪss! sɴᴀᴀᴀᴋᴇᴇ!!!**🐍\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)     
			elif(count==38):
				count=9
				print('\t\t**ʜɪss! sɴᴀᴀᴀᴋᴇᴇ!!!**🐍\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)
			elif(count==40):
				count=68
				print('\t\t**ɢᴏᴛᴄʜᴀ ʟᴀᴅᴅᴇʀ!**🛤\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)
			elif(count==52):
				count=81
				print('\t\t**ɢᴏᴛᴄʜᴀ ʟᴀᴅᴅᴇʀ!**🛤\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)
			elif(count==65):
				count=46
				print('\t\t**ʜɪss! sɴᴀᴀᴀᴋᴇᴇ!!!**🐍\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)
			elif(count==93):
				count=64
				print('\t\t**ʜɪss! sɴᴀᴀᴀᴋᴇᴇ!!!**🐍\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)
			elif(count==89):
				count=70
				print('\t\t**ʜɪss! sɴᴀᴀᴀᴋᴇᴇ!!!**🐍\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)
			elif(count==76):
				count=97
				print('\t\t**ɢᴏᴛᴄʜᴀ ʟᴀᴅᴅᴇʀ!**🛤\t\t')
				print('ʏᴏᴜ ᴀʀᴇ ᴀᴛ:',count)
			elif(count==100):
				print('\t\t\t***** ʏᴏᴜ ᴡᴏɴ!🎖',a,'!  *****\t\t\t')
				break
			elif(count>100):
				count=count-r
				print('ᴛʜᴀᴛs ᴍᴏʀᴇ ᴛʜᴇɴ ʜᴜɴᴅʀᴇᴅ!')	
		else:
			print("\n","-"*42)
			print('ᴡʀᴏɴɢ ᴋᴇʏ!🚫')
			print("-"*42)            



def rps():
	import random
	count=0
	cscore=0
	x={1:'rock',2:'paper',3:'scissor'}
	print("\n\t\t\t*******𝙇𝙀𝙏'𝙎 𝙂𝙊!!!*******\n")

	while True:
		print(a,"!")
		p=input('ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ:')

		c=x[random.randint(1,3)]

		print(a,"! ᴄʜᴏᴏsᴇ:",p,"\nsᴋᴜʟʟʏ ᴄʜᴏᴏsᴇ:",c)

		if(p==c):
			print('\t\t**ᴅʀᴀᴡ!**')
		elif(p=='rock' and c=='paper'):
			print('\t\t ## ʏᴏᴜ ʟᴏsᴇ!😵 ##')
			cscore=cscore+1
		elif(p=='rock' and c=='scissor'):
			print('\t\t ## ᴡɪɴɴᴇʀ ᴡɪɴɴᴇʀ ᴄʜɪᴄᴋᴇɴ ᴅɪɴɴᴇʀ!🍗 ##')
			count=count+1
		elif(p=='paper' and c=='rock'):
			print('\t\t## ᴡɪɴɴᴇʀ ᴡɪɴɴᴇʀ ᴄʜɪᴄᴋᴇɴ ᴅɪɴɴᴇʀ!🍗 ##')
			count=count+1
		elif(p=='paper' and c=='scissor'):
			print('\t\t ## ʏᴏᴜ ʟᴏsᴇ!😵 ##')
			cscore=cscore+1
		elif(p=='scissor' and c=='rock'):
			print('\t\t ## ʏᴏᴜ ʟᴏsᴇ!😵 ##')
			cscore=cscore+1
		elif(p=='scissor' and c=='paper'):
			print('\t\t ## ᴡɪɴɴᴇʀ ᴡɪɴɴᴇʀ ᴄʜɪᴄᴋᴇɴ ᴅɪɴɴᴇʀ!🍗 ##')
			count=count+1
		else:
			print('\n\t ʙᴏʀᴇᴅ?')
			
			print("\t\t## sᴄᴏʀᴇs  ##")
			print(a,": ",count,"Skully: ",cscore)
			if(count>cscore):
				print("\t\t\tʏᴏᴜ ɴᴀɪʟᴇᴅ ɪᴛ!🎖",)
				
			elif(count<cscore):
				print("\t\t\tsᴋᴜʟʟʏ ᴡᴏɴ!🎖")

			else:
				print('\n\n\n**ᴅʀᴀᴡ!**')	
			exit()							
			
def selfie():
	import os
	from time import sleep

	def mymail():
			import smtplib 
			from email.mime.multipart import MIMEMultipart 
			from email.mime.text import MIMEText 
			from email.mime.base import MIMEBase 
			from email import encoders 
			   
			fromaddr = "thennavanpmohan@gmail.com"
			toaddr = "thennavanpmohan@gmail.com"
			   

			msg = MIMEMultipart() 
			 
			msg['From'] = fromaddr 
			  

			msg['To'] = toaddr 
			  

			msg['Subject'] = "𝐂𝐀𝐏𝐓𝐔𝐑𝐄𝐃!"
			  

			body = "𝙷𝙴𝚁𝙴'𝚂 𝚈𝙾𝚄𝚁 𝚂𝙴𝙻𝙵𝙸𝙴! \n\n 𝓢𝓔𝓝𝓣 𝓑𝓨 𝓢𝓚𝓤𝓛𝓛𝓨!💀"
			  

			msg.attach(MIMEText(body, 'plain')) 
			  
			  
			filename = "nobody.jpg"
			attachment = open("/home/dl116/Desktop/nobody.jpg", "rb") 
			  

			p = MIMEBase('application', 'octet-stream') 
			  

			p.set_payload((attachment).read()) 
			  

			encoders.encode_base64(p) 
			   
			p.add_header('Content-Disposition', "attachment;filename= INTRUDER") 
			  

			msg.attach(p) 
			  

			s = smtplib.SMTP('smtp.gmail.com', 587) 
			  

			s.starttls() 
			  

			s.login(fromaddr,"GMAIL1943") 
			  

			text = msg.as_string() 
			  

			s.sendmail(fromaddr, toaddr, text) 
			s.quit() 
			return


	def takesnap():
		os.system("fswebcam -F 4 /home/dl117/Desktop/ten.jpg")
		return

	for i in range(1):
		takesnap()
		mymail()
		sleep(5)

from time import sleep
print('\t\t\t\t\t\t\t       .𝐞𝐝"""" """$$$$𝐛𝐞.')
print('\t\t\t\t\t\t\t     -"           ^""**$$$𝐞.')
print('\t\t\t\t\t\t\t   ."                   \'$$$𝐜')
print('\t\t\t\t\t\t\t  /                      "4$$b')
print('\t\t\t\t\t\t\t d  3                      $$$$')
print('\t\t\t\t\t\t\t $  *                   .$$$$$$')
print('\t\t\t\t\t\t\t.$  ^c           $$$$$e$$$$$$$$.')
print('\t\t\t\t\t\t\td$L  4.         4$$$$$$$$$$$$$$b')
print('\t\t\t\t\t\t\t$$$$b ^ceeeee.  4$$ECL.F*$$$$$$$')
print('\t\t\t\t\t\t\t$$$$P d$$$$F $ $$$$$$$$$- $$$$$$')
print('\t\t\t\t\t\t\t3$$$F "$$$$b   $"$$$$$$$  $$$$*"')
print('\t\t\t\t\t\t\t $$P"  "$$b   .$ $$$$$...e$$')
print('\t\t\t\t\t\t\t  *c    ..    $$ 3$$$$$$$$$$eF')
print('\t\t\t\t\t\t\t    %ce""    $$$  $$$$$$$$$$*')
print('\t\t\t\t\t\t\t     *$e.    *** d$$$$$"L$$')
print('\t\t\t\t\t\t\t      $$$      4J$$$$$% $$$')
print('\t\t\t\t\t\t\t     $"\'$=e....$*$$**$cz$$"')
print('\t\t\t\t\t\t\t     $  *=%4.$ L L$ P3$$$F')
print('\t\t\t\t\t\t\t     $   "%*ebJLzb$e$$$$$b')
print('\t\t\t\t\t\t\t      %..      4$$$$$$$$$$')
print('\t\t\t\t\t\t\t       $$$e   z$$$$$$$$$$')
print('\t\t\t\t\t\t\t        "*$c  "$$$$$$$P"')
print('\t\t\t\t\t\t\t          """*$$$$$$$"')
print("\n")


print("\t║▌║▌║█│▌║▌║▌║█│▌║▌║▌║█│▌ 𝐒 𝐊 𝐔 𝐋 𝐋 𝐘  : 𝐓 𝐇 𝐄  𝐀 𝐑 𝐓 𝐈 𝐅 𝐈 𝐂 𝐈 𝐀 𝐋   𝐈 𝐍 𝐓 𝐄 𝐋 𝐋 𝐈 𝐆 𝐄 𝐍 𝐂 𝐄  ║▌║▌║█│▌║▌║▌║█│▌║▌║▌║█│▌║▌║▌║█│▌")


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
name()
print(a,"......",c)
print("-"*30)
	

read()	

'''b=input("\nyour age?")
c=input("\nyour gender?")'''

while True:
	d=None
	x=None
	repeat()
	#heyskully()
	#print("tell me:",x)
	d=input("Tell me :")
	#d=x				
	if(d=="tell me a joke" or d=="joke" or d=="meme"):
		print("\n","-"*32)
		print("\tɪ ʜᴀᴠᴇ ɢᴏᴛ ᴘʟᴇɴᴛʏ ᴏғ ᴛʜᴇᴍ!😉")
		print("-"*32)
		meme()
		print("\n","-"*20)
		e=input(" ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴏʀᴇ?")
		print("-"*20)
		if(e=='Y' or e=='y' or e=='Yes' or e=='yes' or e=='ya' or e=='yup' or e=='yea'):
			print("\nᴛʜᴀᴛ's ɢᴏᴏᴅ! ɪ ʟɪᴋᴇ ᴛʜᴀᴛ")
			meme()
			continue
		else:
			print("\n","-"*42)
			print("\nɴᴏ ᴘʀᴏʙʟᴇᴍ! ʏᴏᴜ ᴄᴀɴ ᴛʀʏ ᴏᴛʜᴇʀ ᴛʜɪɴɢs ᴛᴏᴏ!")
			print("-"*42)
			continue

	elif(d=="take a selfie" or d=="selfie" or d=="click a pic" or d=="picture" or d=="photo" or d=="take"):
		selfie()
		continue

	elif(d=="play a game" or d=="game" or d=="play" or d=="rock" or d=="snake"):
		print("\nʜᴇʀᴇ's ᴡʜᴀᴛ ɪ ᴋɴᴏᴡ ᴛᴏ ᴘʟᴀʏ:")
		print("\tsɴᴀᴋᴇ ᴀɴᴅ ʟᴀᴅᴅᴇʀ \n\t ʀᴏᴄᴋ ᴘᴀᴘᴇʀ sᴄɪssᴏʀ \n\t ᴛɪᴄ ᴛᴀᴄ ᴛᴏᴇ")
		print(" so...")
		sleep(1)
		l=input("ᴡʜᴀᴛ ᴅɪᴅ ʏᴏᴜ ᴘʟᴀɴ ᴛᴏ ᴘʟᴀʏ?")
		if(l=="snake and ladder" or l=="Snake & ladder" or l=="snake" or l=="ladder" ):
			sleep(1)
			print("\n","-"*42)
			print("ʏᴏᴜ sᴇᴇ! ɪ'ᴍ ɢᴏɴɴᴀ ᴡɪɴ!😎😎")
			print("-"*42)  
			ladder()
			continue
		elif (l=="rock paper scissor" or l=="rps" or l=="Rock" or l=="paper" or l=="scissor"):
			sleep(1)
			print("\n","-"*42)
			print("ɪ ᴀᴍ ᴘʀᴏ ɪɴ ᴛʜɪs ɢᴀᴍᴇ!😎😎")
			print("-"*42)
			rps()
			continue
		elif(l=="tic tac toe" or l=="x and o" or l=="ttt" or l=="tic" or l=="tac" or l=="toe"):
			print("\n","-"*22)
			print("𝙇𝙀𝙏'𝙎 𝙎𝙀𝙀 𝙒𝙃𝙊 𝙒𝙄𝙉𝙎 🔥🔥🔥")
			print("-"*22)
			tic()
			continue		

	elif(d=="search for anything" or d=="google" or d=="search" or d=="anything" or d=="browser"):
		sleep(1)
		google()
		continue
	elif(d=="calculate" or d=="calculator" or d=="calci" or d=="add" or d=="subtract" or d=="maths"):
		sleep(1)
		print("\n","-"*42)
		print("ɪ ᴀᴍ ᴀ ᴍᴀᴛʜs ғʀᴇᴀᴋ! ʏᴏᴜ ᴋɴᴏᴡ!")
		print("-"*42)
		calcii()
		continue
	elif(d=="play a video" or d=="video" or d=="map" or d=="map"):
		sleep(1)
		print("\n","-"*42)
		print("ɪ ᴄᴀɴ sɪɴɢᴇʀ ʙᴇᴛᴛᴇʀ ᴛʜᴀɴ ᴊᴜsᴛɪɴ ʙɪᴇʙᴇʀ ʙᴜᴛ ɪ ᴡɪʟʟ ʟᴇᴛ ʏᴏᴜᴛᴜʙᴇ ᴅᴏ ᴛʜᴇ ᴡᴏʀᴋ!")
		print("-"*42)
		youtube()
		continue
	elif(d=="shopping" or d=="shop" or d=="market" or d=="amazon" or d=="something"):
		print("\nᴡʜɪᴄʜ ᴏɴᴇ ᴅᴏ ʏᴏᴜ ᴘʀᴇғᴇʀ?")
		sleep(1)
		print("\nᴀᴍᴀᴢᴏɴ or ғʟɪᴘᴋᴀʀᴛ or ᴇʙᴀʏ")
		
		x=input("tell tell!")
		if(x=="amazon"):
			print("\n","-"*42)
			print("ɪ ᴀʟᴡᴀʏs ᴘʀᴇғᴇʀ ᴀᴍᴀᴢᴏɴ ʏᴏᴜ ᴋɴᴏᴡ!😊😊")
			print("-"*42)
		elif(x=="flipkart"):
			print("\n","-"*42)
			print("\nɪ ᴀʟᴡᴀʏs ᴘʀᴇғᴇʀ ғʟɪᴘᴋᴀʀᴛ ʏᴏᴜ ᴋɴᴏᴡ!😊😊")
			print("-"*42)
		elif(x=="ebay"):
			print("\n","-"*42)
			print("ɪ ᴀʟᴡᴀʏs ᴘʀᴇғᴇʀ ᴇʙᴀʏ ʏᴏᴜ ᴋɴᴏᴡ!😊😊")
			print("-"*42)
			shopping()					
			
			
	elif(d=="maps" or d=="map" or d=="map" or d=="map" or d=="map"):
		maps()
		continue

	else:
		print("\n","-"*42)
		print("sᴏʀʀʏ! ɪᴅ ᴅɪᴅɴ'ᴛ ɢᴇᴛ ᴛʜᴀᴛ! ᴡʜʏ ᴅᴏɴ'ᴛ ʏᴏᴜ ᴛʀʏ ᴀɢᴀɪɴ!")
		print("-"*42)
		continue		