#Write a Python program to accept a string and count the number of vowels in it. 
x = input("String: ")
n = 0
for i in x:
    if i in "aeiouAEIOU":
        n+=1
print("No of vowels: ",n)