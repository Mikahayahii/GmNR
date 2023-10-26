def math():
  while True:
    num1 = int(input('Первое число?: '))
    num2 = int(input('Второе число?: '))
    action = input('Действие?: ')
 
    if action == '+':
      print(num1, '+', num2, '=', num1 + num2)
    elif action == '-':
      print(num1, '-', num2, '=', num1 - num2)
    elif action == '*':
      print(num1, '*', num2, '=', num1 * num2)
    elif action == '/':
      print(num1, '/', num2, '=', num1 / num2)
    else:
      print('Ошибка. Такой операции не существует. Попробуйте ещё раз')
      math()
 
math()