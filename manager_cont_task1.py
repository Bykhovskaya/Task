#менеджер контекста, печатающий на экран: врямя запуска кода, время окончания, потраченное время

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
        s = [x for x in range(10000000)]
