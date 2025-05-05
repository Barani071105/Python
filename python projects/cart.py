name=input("Enter your name:")
item=input("Enter your product name:")
price=float(input("Enter the price of the product:"))
quantity=int(input("Enter the quantity:"))
result=price*quantity
print("the name {} and your product {} and net price {} ".format(name,item,result))