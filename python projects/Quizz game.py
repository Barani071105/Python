print("Welcome to quizz game!!!")
point=0
player=input("Do you want to play?")
player=player.lower()
if player!="yes":
    print("Incorrect password")
    exit()
else:
    print("Ok lets start start!!!")
       
Question1=input("How many days in a week?")
if Question1=="seven":
     print("Wonderful answer")   
     point=point+1
else:
     print("Wrong")
Question2=input("How many  months in a year?")
if Question2 == "twelve":
     print("Absolutely correct")      
     point+=1
else:
    print("OOPS")



print("your total score:",point)           
               
             