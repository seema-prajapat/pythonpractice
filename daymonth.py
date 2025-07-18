month=int(input("Enter a month(1-12):"))
year = int(input("Enter a year:"))
if month in [1,3,5,7,8,10,12]:
  print("31 Days")
elif month in[4,6,9,11]:
  print("30 Days")  
elif month == 2:
  if(year % 4==0 and year % 100 != 0):
    print("29 Days")
  else:
    print("28 Days")     
else:
  print("Invalid month")  