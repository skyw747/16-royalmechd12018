import random
count=0
cscore=0
a={1:'rock',2:'paper',3:'scissor'}

while True:
	p=input('enter your choice:')

	c=a[random.randint(1,3)]

	print("you chose:",p,"\ncomputer chose:",c)

	if(p==c):
		print('\t\t   **Draw!**  ')
	elif(p=='rock' and c=='paper'):
		print('\t\t ## you lose! ##')
		cscore=cscore+1
	elif(p=='rock' and c=='scissor'):
		print('\t\t ## you win! ## ')
		count=count+1
	elif(p=='paper' and c=='rock'):
		print('\t\t## you win! ##')
		count=count+1
	elif(p=='paper' and c=='scissor'):
		print('\t\t ## you lose! ## ')
		cscore=cscore+1
	elif(p=='scissor' and c=='rock'):
		print('\t\t ## you lose! ## ')
		cscore=cscore+1
	elif(p=='scissor' and c=='paper'):
		print('\t\t ## you win! ## ')
		count=count+1
	else:
		print('\n\t bored?')
		print("\t\t## Scores  ##")
		print("yours: ",count,"computer: ",cscore)
		if(count>cscore):
			print("you nailed it!")
		elif(count<cscore):
			print("computer won!")
		else:
			print('its draw!')		
		exit()						