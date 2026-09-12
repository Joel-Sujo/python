#Write a Python program to count the number of occurrences of a particular character in a string. 

x = input("Enter string: ")
y = input("Enter the character to be counted")

n = 0
for i in x:
    if y == i:
        n+=1
print("No of occurances of that character is: ",n)