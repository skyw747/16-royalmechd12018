a=int(input('Enter Your Marks:'))

print('Your grade is :')

if(a>=90):
	print('A+')
#elif:stands for else if
#used for more than one conditional statement
if(a>=80):
	print('A')
elif(a>=70):
	print('B+')
elif(a>=60):
	print('B')
elif(a>=50):
	print('C')
else:
	print('Fail!')					
