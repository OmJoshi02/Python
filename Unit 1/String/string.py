#Single quoted string
str1 = 'Hello'
print(str1)
print()
#Double quoted string
str2 = "Hello"
print(str2)
print()
#Tripple quoted string
str3 = """Hello everyone
        My name is Om
        I'm pursuing Computer Science degree in D.Y.Patil College of Engineering and Technology, Kolhapur"""
print(str3)
print()
#Simple string output

str = "Hello world"
#Positive Indexing
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print()

#Negative Indexing
print(str[-5])
print(str[-4])
print(str[-3])
print(str[-2])
print(str[-1])
print()

#String functions

s1 = "hello"
s2 = "HELLO"
s3 = "xxxHelloxxx"

print(s1.capitalize()) #Converts first character capital
print(s2.casefold()) #Converts string into lower case
print(s1.count("l")) # returns the no. of times letter appeared
print(s2.lstrip("x")) #Removes unwanted characters, letters, whitespaces, spaces
print(s1.replace("l", "L")) #Replaces the current letter with updated letter
print(s1.upper()) #Converts string to upper cases
print(s2.swapcase()) #Changes upper cases to lower and lower to upper
print(s2.lower()) #Converts string to lower cases
print(s2.find("L")) #Finds requested value in string and returns the index of that character
print(str.split()) #Seperates two different words into 