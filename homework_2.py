entered_number = input('Введіть 4-х значне число')

value_thousands = int(entered_number)//1000
value_hundreds = (int(entered_number)//100)%10
value_tens = (int(entered_number)//10)%10
value_units = int(entered_number)%10

print(f"{value_thousands}\n{value_hundreds}\n{value_tens}\n{value_units}")
