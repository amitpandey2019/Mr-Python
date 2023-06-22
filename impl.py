num1= int(input("Enter First number"))
num2= int(input("Enter Second number"))
num3= int(input("Enter Third number"))
 
 def largest(x,y,z):
 if(num1>num2) and (num1>num3):
 return num1
elif num2 > num3:
return num2
else
return num3
print("Largest number is "+str(largest(num1,num2,num3)))