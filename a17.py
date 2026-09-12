#Write a Python program to check whether a particular character is present in a string. 

x = input("Enter string: ")
y = input("The character to be searched: ")
if x.find(y) != -1:
    print("Character is present")
else:
    print("Character not present")