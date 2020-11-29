First_Name =input(' Enter first name')
Last_Name = input(' Enter last name')
 
str = First_Name + ' ' + Last_Name

stringlength=len(str) # calculate length of the list
slicedString=str[stringlength::-1] # slicing 
print (slicedString) # print the reversed string