def sum_of_digits(number):
    
    number_str = str(number)
        total = 0

    for char in number_str:
        
        total += int(char)
    
    return total

number = int(input("Enter a number: "))

result = sum_of_digits(number)

print("The sum of digits of the number", number, "is:", result)
