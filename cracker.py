import math
import os
def combo():
	first = (math.ceil(resLoc)+5)%40
	second = []
	third = []

	mod = first%4

	for i in range(0,4):
		if ((10*i)+firstDigit)%4 == mod:
			third.append((10*i)+firstDigit)

		if ((10*i)+secondDigit)%4 == mod:
			third.append((10*i)+secondDigit)
	#print(first)
	ty = int(input('Is the third digit ' + str(third[0]) + ' or is it ' + str(third[1])+' ?:'))

	if ty == third[0]:
		third=ty
		for i in range(0,10):
			tmp = ((mod+2)%4)+(4*i)
			if (third+2)%40 != tmp and (third-2)%40 != tmp:
				second.append(tmp)

	elif ty == third[1]:
		third = ty
		for i in range(0,10):
			tmp = ((mod-2)%4)+(4*i)
			if (third+2)%40 != tmp and (third-2)%40 != tmp:
				second.append(tmp)

	os.system('cls' if os.name =='nt' else clear)
	print('======================================')
	print('You can now crack your master padlock!')
	print('======================================\n')

	print('Your first digit is: '+str(first)+'\n')
	print('Your second digits are: ')
	print(*second)
	print('\n')
	print('Your third digit is: '+str(third))

firstDigit = int(input('Enter first digit: '))
secondDigit = int(input('Enter second Digit: '))
resLoc = int(input('Enter resistant location: '))

if firstDigit and secondDigit and resLoc:
	combo()




