#Write a Python program to accept a string and check whether it is a palindrome. 

x = input("String: ")
if x == x[::-1]:
    print("Palindrom")
else:
    print("Not palindrome")