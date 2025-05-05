import random

print("Welcome to random password genrator!!!")
charsnums="ABCDEFFGHIJKLMNOPQRSTWUVXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
noofpass=int(input("Enter how many password you need:"))
passlen=int(input("Enter how length you need:"))

for x in range(noofpass):
    pwd=""
    for y in range(passlen):
      pwd="".append(random.choice(charsnums))
     print(pwd)
    