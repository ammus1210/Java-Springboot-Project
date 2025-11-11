def add_numbers(a, b):
  """A simple function to add two numbers."""
  return a + b

def main():
  """The main function of the script."""
  print("This is the main script.")
  num1 = 10
  num2 = 5
  result = add_numbers(num1, num2)
  print(f"The sum of {num1} and {num2} is: {result}")

# This is the entry point of the script.
# The code inside this block will only run when main.py is executed directly.
if __name__ == '__main__':
  main()
