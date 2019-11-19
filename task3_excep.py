documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }


#функция вывода владельца документа
def get_name_doc():
    doc = input('\nВведите номер документа: ')
    try:
        check = next(item for item in documents if item['number'] == doc)
        print('Документ принадлежит: {}'.format(check['name']))
    except:
        print('Документ не найден')

#функция добавления в каталог
def add_doc():
     shelf_number = input('Введите номер полки:')
     doc_number = input('Введите номер документа:')
     doc_type = input('Введите тип документа:')
     owner_name = input('Введите имя владельца документа:')

     directories[shelf_number] = directories.get(shelf_number, []) + [doc_number]

     a = {"type":doc_type, "number":doc_number, "name":owner_name}
     documents.append(a)
     print("\nДокумент добавлен")


# функция вывода списка документов
def list_people():
    print('\nСписок всех документов в каталоге: ')
    for people_doc in documents:
        print(people_doc.get("type"), '"'+people_doc.get("number")+'"' , '"'+people_doc.get("name")+'"')

# функция добавления новой полки
def add_new_shelf():
    user_input_shelf = input('\nДля создания новой полки введите ее номер:')
    if user_input_shelf in directories.keys():
        print('Такая полка уже есть, введите другое значение')
        add_new_shelf()
    if user_input_shelf not in directories.keys():
        directories[user_input_shelf] = []  # добавляет в каталог
        print('\nНовая полка создана')
        main()

#функция вывода полки

def get_key_shelf(directories):
    doc_number = input('\nВведите номер документа:  ')
    doc_dir = ''
    for k, v in directories.items():
        for number in v:
            if number == doc_number:
                doc_dir = k
    if doc_dir != '':
        print('Полка', doc_dir)
    else:
        print('Документа не существует')

#функция вывода владельцев документов (исключаем ошибку)
def get_name():
           for item in documents:
               try:
                   print(item['name'])
               except KeyError:
                   print('Имя для владельца не определено')

def main():
      while True:
          user_input = input('\nЗдраствуйте!'
                             '\nВведите команду: '
                      '\nдля получения имени по номеру документа - 1:  '
                      '\nдля получения списка всех документов - 2:   '
                      '\nдля получения номера полки документа - 3:   '
                      '\nдля добавления документа в каталог - 4:     '
                      '\nдля добавления новой полки - 5:'
                      '\nдля вывода владельцев документов - 6         ')
          if user_input == '1':
              get_name_doc()
          if user_input == '2':
              list_people()
          if user_input == '3':
              get_key_shelf(directories)
          if user_input == '4':
              add_doc()
          if user_input == '5':
              add_new_shelf()
          if user_input == '6':
              get_name()
              

main()
