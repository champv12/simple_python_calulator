def numbers_input():
    """Prompt the user for the number of inputs and validate the input."""
    while True:
        try:
            numbers = int(input("How many numbers to calculate? "))
            if numbers <= 0:
                print("Enter a number greater than zero.")
                continue
            return numbers
        except ValueError:
            print("Please enter a valid numerical value.")

def values_input(count):
    """Prompt the user to input `count` numbers and return them as a list."""
    numbers_list = []
    for i in range(count):
        while True:
            try:
                value = int(input(f"Enter number {i + 1}: "))
                if value <= 0:
                    print("Enter a number greater than zero.")
                    continue
                numbers_list.append(value)
                break
            except ValueError:
                print("Please enter a valid numerical value.")
    return numbers_list

def calculate():
    """Main function to get inputs, calculate the sum, and display the result."""
    count = numbers_input()
    values = values_input(count)
    total = sum(values)
    print(f"The sum of the entered numbers is: {total}")

# Run the program
calculate()