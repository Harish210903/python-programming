string=input("enter the para:")
str1=string.split("...")
str1.pop()
print("total number of lines:",len(str1))
count=0
for i in str1:
 str2=i.split()
 for j in str2:
  if j[0]=="b":
   count=count+1
print("number of sentence that start with letter b:",count)
