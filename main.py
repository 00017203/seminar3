# 
def converter_to_decimal(number, base):
    temp = int(number, base)
    print(temp)


numberInput = input("Enter the number: ")
baseInput = int(input("Enter the base: "))
converter_to_decimal(numberInput, baseInput)