print("Welcome to BARANI's Bank\n\n Please insert your card")
password="baranii@2005"
pin=input("Enter your pesonal pin:")
balance=10000
choice=0
if password==pin:
    print("Correct password") 
    while choice!=4:
     print("****MENU****")
     print("BALANCE==1")
     print("DEPOSIT==2")
     print("WITHDRAWL==3")
     print("EXIT==4")
     choice=(input("Enter your choice:"))
     if choice=="1":
        print(f"your account balance:{balance}")
     elif(choice=="2"):
        deposit=int(input("Enter amount your going to deposit:\n"))
        balance=balance+deposit
        print("total account balance:",balance)   
     elif(choice=="3"):
        withdrawl=int(input("Enter amount going to withdraw:"))
        balance =balance-withdrawl
        print(balance)
     else:
        print("Please remove your card")       
else:
    print("INCORRECT PASSWORD")         