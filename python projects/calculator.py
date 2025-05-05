print("Welcome to calculator!!!")
ch=0
while (ch!=4):
 print("####chosse operation####")
 print("1 == add")
 print("2 == sub")
 print("3 == multi")
 print("4 == div")
 ch=int(input("Enter your choice:"))
 num1=int(input("Enter the first number:"))
 num2=int(input("Enter the second number:"))
 if(ch==1):
     print("sum:",num1+num2)
 elif(ch==2):
     print("sub:",num1-num2)
 elif(ch==3):
     print("multi:",num1*num2)
 elif(ch==4):
     print("div:",num1/num2)
 else:
     print("invalid choice")
           