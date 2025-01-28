[200~def calculator():
      print("Welcome to the Calculator!")
      print("Select operation:")
      print("1. Addition (+)")
      print("2. Subtraction (-)")
      print("3. Multiplication (*)")
      print("4. Division (/)")
      
      while True:
          try:
              # Take input from the user
              choice = input("Enter choice (1/2/3/4): ")
              
              if choice not in ('1', '2', '3', '4'):
                  print("Invalid input. Please enter a valid choice.")
                  continue

              # Input numbers
              num1 = float(input("Enter first number: "))
              num2 = float(input("Enter second number: "))

              # Perform calculations
              if choice == '1':
                  print(f"The result is: {num1 + num2}")
              elif choice == '2':
                  print(f"The result is: {num1 - num2}")
              elif choice == '3':
                  print(f"The result is: {num1 * num2}")
              elif choice == '4':
                  if num2 != 0:
                      print(f"The result is: {num1 / num2}")
                  else:
                      print("Error: Division by zero is not allowed.")

              # Ask the user if they want to perform another calculation
              next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
              if next_calculation != 'yes':
                  print("Thank you for using the calculator. Goodbye!")
                  break

          except ValueError:
              print("Invalid input. Please enter numeric values.")

  # Run the calculator
  calculator()

