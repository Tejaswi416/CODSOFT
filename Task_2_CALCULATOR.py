def calculator():
#   A simple calculator that can perform basic arithmetic operations.

  # Get the values of two numbers from the user.
  A = int(input("Enter the value for first number: "))
  B = int(input("Enter the value for second number: "))

  # Get the operation from the user.
  operation = input("choose the operation from the given options in bracket (+, -, *, /): ")

  # Perform the calculation and display the result.
  if operation == "+":
    result = A + B
  elif operation == "-":
    result = A - B
  elif operation == "*":
    result = A * B
  elif operation == "/":
    result = A / B
  else:
    print("Invalid operation.")
    return

  # Print the result.
  print("The result is", result)


if __name__ == "__main__":
  calculator()
