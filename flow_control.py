# Ведення першого числа

try:
    operand_1 = float(input('Введіть перше число: \n'))
except:
    operand_1 = input('Ви ввели неправильне перше число. Введіть ціле або десяткове число: \n')

# Ведення ариффметичної операції

operation = input('Введіть математичну операцію. Додавання +, віднімання -, множення *, ділення /, степінь pow \n')

if operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '**':
    operation = input('Неправильний знак. Введіть +, -, *, /, '**': \n')

# Ведення другого числа

try:
    operand_2 = float(input('Введіть друге число: \n'))
except:
    operand_2 = input('Ви ввели неправильне друге число. Введіть ціле або десяткове число: \n')

# Виконнання операції першого числа з другим
try:
    if operation == '+':
        result = operand_1 + operand_2
    elif operation == '-':
        result = operand_1 - operand_2
    elif operation == '*':
        result = operand_1 * operand_2
    elif operation == '/':
        result = operand_1 / operand_2
    elif operation == '**':
        result = operand_1**operand_2
except ZeroDivisionError:
    print('На нуль ділити не можна.')

# Виведення результату

else:
    if (result % 1) == 0.0:
        result = int(result)
        print(f'Ваш результат: {result}, тип: {type(result)}')
    else:
     print(f'Ваш результат: {result}, тип: {type(result)}')
