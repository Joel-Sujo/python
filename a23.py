#Write a Python program to accept a word and print its characters at odd index positions. 

x = input("Word: ")
for i in range(len(x)):
    if i%2 != 0:
        print(x[i],"\n")