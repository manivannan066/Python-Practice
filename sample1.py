# Simple Calculator Program

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("1. Addition (+)")
print("2. Subtraction (-)")
#print("3. Multiplication (*)")
#print("4. Division (/)")

choice = input("Select your operation (1/2/3/4): ")

if choice == "1":
    print("Addition =", num1 + num2)

elif choice == "2":
    print("Subtraction =", num1 - num2)

elif choice == "3":
    print("Multiplication =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid choice")