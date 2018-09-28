import random
 
count=0

def myroll():
	return random.randint(1,6)

while(count<=100):
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
			print('\t\t\t***** You Won!!  *****\t\t\t')
			break
		elif(count>100):
			count=count-r
			print('thats more then hundred!')	
	else:
		print('wrong key!')
		exit()		                               


