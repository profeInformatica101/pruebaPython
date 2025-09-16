# Esto es una funcion
def lower_num(num1, num2):
    if num1 <= num2 :
        lowest = num1
    else:
        lowest = num2
    return lowest

# Esto es una llamada a una funcion
first_number = int (input("Enter the first number:"))
second_number = int (input ("Enter the second number:"))
print("The lowest is " + str(lower_num(first_number, second_number)))
