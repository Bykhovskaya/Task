import datetime

class Timer(object):
    def __init__(self, task):
        self.task = task
    def __enter__(self):
        self.start = datetime.datetime.now()
    def __exit__(self, type, value, traceback):
        self.end = datetime.datetime.now()
        print("Время начала:", self.start)
        print("Время окончания:", self.end)
        print(self.task, self.end - self.start)

if __name__ == '__main__':
    with Timer("Время выполнения"):

        user_input = input('Введите знак вычисления (+, -, *, /) и два целых положительных числа через пробел')
        input_list = user_input.split(' ')

        assert input_list[0] in ('+', '-', '*', '/'), 'Введен некорректный оператор. Повторите ввод'

        try:
            a = int(input_list[1])
            b = int(input_list[2])
            if a < 0 or b < 0:
                print('Вы ввели отрицательное число')
            if input_list[0] == '+' and a > 0 and b > 0:
                result = a + b
                # print(result)
            if input_list[0] == '-' and a > 0 and b > 0:
                result = a - b
            if input_list[0] == '*' and a > 0 and b > 0:
                result = a * b
            if input_list[0] == '/' and a > 0 and b > 0:
                result = a / b
            print('Результат вычисления', result, '\n')
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
