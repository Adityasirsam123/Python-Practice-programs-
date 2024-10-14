year = int(input("Enter an year"))
# year divided by 100 means century year (end with 00)
# and it is divided by 400 is leap year
if (year % 400 == 0) and (year % 100 ==0):
 print(f"{year} is leap year".format(year))
 # not divided by 100 means not century year
 #year divided by 4 is leap year
elif (year % 4 == 0) and (year % 100 !=0):
 print(f"{year} is a leap year")
 # if not divided by both 400 and 4 then year is not leap year
else:
 print(f"{year} is not leap year")