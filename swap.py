#swap variables 
a = int(input("enter an integer (a:)"))
b = int(input("enter an integer (b:)"))
print(f"values before swaping: a= {a},b= {b}")
# swapping in process
temp =a
a=b
b = temp
#display swaped values
print(f"values after swaping: a= {a},b= {b}")