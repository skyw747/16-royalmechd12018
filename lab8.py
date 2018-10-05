a=['1','2','3','4','5','6','7','8','9']
def print_board():
	print('_',a[0],'_|_',a[1],'_|_',a[2],'_')
	print('_',a[3],'_|_',a[4],'_|_',a[5],'_')
	print(' ',a[6],' | ',a[7],' | ',a[8],' ')



player1turn = True

while True:
	print_board()

	x=input('where to put x?:')
	if(x in a):
		if(a[int(x)-1]=='x' or a[int(x)-1]=='o'):
			print('snap! place taken! choose another one!')
			continue
		else:
			if player1turn:
				a[int(x)-1] ='x'
				player1turn = not player1turn
			else:
				a[int(x)-1] ='o'
				player1turn = not player1turn
			for i in (0,3,6):
					if(a[i] == a[i+1] and a[i] == a[i+2]):
						print_board()
						print('Game over')
						exit()
			for i in range(3):
					if(a[i] == a[i+3] and a[i] == a[i+6]):
						print_board()
						print('Game over')
						exit()
			if(a[0] == a[4] and a[0] == a[8]):
					print_board()
					print("Game over")
			elif(a[2] == a[4] and a[2] == a[6]):
					print_board()
					print("Game over")					

	else:
		continue		


