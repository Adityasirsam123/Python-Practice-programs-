# program to check whether number is prime or not
num = int(input("Enter integer"))
#define flag variable

flag = False
if flag ==1:
    print(f"{num}, is not prime number")
elif num >1 :
    #checks for factors
    for i in range (2,num):
        if (num %i ==0):
            flag = True # if the factor is found then break out the loop
if flag:
    print(f"{num}, is not prime number")
else :
    print(f"{num}, is prime number")