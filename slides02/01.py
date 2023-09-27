# work with numbers

number1 = 3
number2 = 2

number3 = number1**number2

# string concatenation
number1_as_a_string = str(number1)
number2_as_a_string = str(number2)
number3_as_a_string = str(number3)

message1 = (
    "raising "
    + number1_as_a_string
    + " to the power "
    + number2_as_a_string
    + " is: "
    + number3_as_a_string
)

# string interpolation
message2 = "raising {n1} to the power {n2} is: {n3}".format(
    n1=number1_as_a_string, n2=number2_as_a_string, n3=number3_as_a_string
)

# string interpolation
message3 = f"raising {number1_as_a_string} to the power {number2_as_a_string} is 🚀 {number3_as_a_string}"

# string parts
type_of_operation = message3[::-1]

print(type_of_operation)
