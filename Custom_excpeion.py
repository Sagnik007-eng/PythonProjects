# define Python user-defined exceptions
class InvalidDateException(Exception):
    "Raised when the input value is less than 18"
    pass
# you need to guess this number

try:
    input_num = int(input("Enter a number: "))
    if input_num >28 :
        raise InvalidDateException
    elif input_num%7==0:
        print("Multiple of 7")
    else:
        print("Correct Num")

except InvalidDateException:
    print("Exception occurred: Invalid Date")