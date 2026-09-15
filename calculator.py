first_number = float(input("Give me back the first number:", ))
operator = input('+, -, *, /:', )
second_number = float(input("Give me back the second number:", ))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        result = "Cannot divide by Zero"
    else:
        result = first_number / second_number

else:
    result = "Invalid operator"

print("Result:", result)