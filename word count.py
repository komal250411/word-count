
# Python3 code to demonstrate 
# to count words in string 
# using split()
 
# initializing string 
test_string = " few things bring out differences between Punjabis and Tamilians than buffet meals.Tamilians see it like any other meal" 

# printing original string
print ("The original string is : " + test_string)
 
# using split()
# to count words in string
res = len(test_string.split())
 
# printing result
print ("The number of words in string are : " + str(res))


