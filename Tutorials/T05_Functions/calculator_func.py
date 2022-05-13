def calculator(num1=0.0, num2=0.0):
    print("addition:", num1 + num2)
    print("Multiplication:", num1 * num2)
    print("Division:", num1 / num2)
    print("Subtraction", num1 - num2)

user_input1 = input("Enter 1st number: ")
user_input2 = input("Enter 2nd number: ")
calculator(float(user_input1), float(user_input2))
input() # Cheat to pause console
