class smart:
	x=[]
	y=[]
	for i in range(0,3):
		name=input('Type Your Name:')
		usn=input('Your USN:')
		x.append(name)
		y.append(usn)
	for j in range(0,3):
		print('\nName:',x[j])
		print('Age:',y[j])
		
p=smart()
	
