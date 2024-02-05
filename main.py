print("Coded by Kriteak Raj")
print("********WELCOME TO CALCULATOR********")

a = float(input("Enter the First number: "))
b = float(input("Enter the second number: "))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divide")

choice = input("Enter what you want(1/2/3/4): ")

if choice == '1' :
    print(a + b)
elif choice == '2' :
    print(a - b)
elif choice == '3' :
    print(a * b)
elif choice == '4' :
    print(a / b)
else : 
    print("The thing you entered is incorrect.Please check your input.")
