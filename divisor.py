choice=1
while choice == 1:
	i=1
	num=int(input("Enter Test Number: "))
	while i<(num/2+1):
		if num%i==0:
			print(i)
		i=i+1
	try:
		print(num)
		choice=int(input("Try Again ?[1=Yes,0=No] Choice: "))
	except:
		print("Invalid Choice")
		choice=1