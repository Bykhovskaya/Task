#реализация Польской нотации для двух положительных чисел

user_input = input('Введите знак вычисления (+, -, *, /) и два целых положительных числа через пробел')
input_list = user_input.split(' ')

assert input_list[0] in ('+', '-', '*', '/'), 'Введен некорректный оператор. Повторите ввод'

try:
        a = int(input_list[1])
        b = int(input_list[2])
        if a < 0 or b < 0:
            print('Вы ввели отрицательное число')
        if input_list[0] == '+' and a > 0 and b > 0:
            result = a+b
            #print(result)
        if input_list[0] == '-' and a > 0 and b > 0:
            result = a-b
        if input_list[0] == '*' and a > 0 and b > 0:
            result = a*b
        if input_list[0] == '/' and a > 0 and b > 0:
            result = a/b
        print(result)
except NameError:
        print('Некорректный ввод данных')
except ValueError:
        print('Некорректный ввод данных')
except ZeroDivisionError:
        print('На ноль делить нельзя')
except IndexError:
        print('Некорректный ввод данных')
except Exception as e:
        print('Исключение', e, 'тип:', type(e))
