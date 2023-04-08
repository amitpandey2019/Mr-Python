num = int(input("Enter a number:"))
# If number is greater than 1
if num > 1:
    # Cheak if factor exist
    for i in range(2,num):
        if(num % i) == 0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")