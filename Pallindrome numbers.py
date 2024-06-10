def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

user_input = input("Enter a number to check if it's a palindrome: ")

if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    number = int(user_input)
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
else:
    print("Invalid input! Please enter a valid integer.")
