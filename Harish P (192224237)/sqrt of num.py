lower_range=int(input("enter the lower range:"))
upper_range=int(input("enter the upper range:"))
if lower_range>upper_range:
 print("invalid input:lower range is greater than upper range.")
else:
 result=[(num,num**2)for num in range(lower_range,upper_range+1)]
 print(result)
