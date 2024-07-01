print("~~~ Simple Calculator~~~")
 
 #input a number from user
val1=float(input("enter a first value:"))
val2=float(input("enter a second value:"))

print("Choose Operation:")
print("a: Press 1 for addition")
print("b: Press 2 for subtraction")
print("c: Press 3 for multiplication")
print("d: Press 4 for division")


choice=int(input("enter a choice from 1-4 :"))

if choice == 1:
    print(val1,"+",val2,"=",val1+val2)


elif choice == 2:
    print(val1,"-",val2,"=",val1-val2)

elif choice == 3:
    print(val1,"*",val2,"=",val1*val2)

elif choice == 4:
    if val2!=0: 
      print(val1,"/",val2,"=",val1/val2)
    else:
     print("Cannot divide by zero:")  

else:
    print("Invalid number:")       

