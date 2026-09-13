#Write a Python program to accept a string and find the frequency of a given character.

x=input("String: ")
y = input("Character: ")
n = 0
for i in x:
    if i == y:
        n+=1
print("Frequency: ",n)