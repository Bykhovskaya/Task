def get_cook_book():
    with open("recipes.txt") as f:
        cook_book = {}
        for line in f:
            keys = line
            number = int(f.readline())
            while number != 0:
                value = f.readline().strip().split('|')
                number -= 1
                if keys.strip() not in cook_book.keys():
                    cook_book[keys.strip()] = list()
                dishes = dict()
                dishes['ingridient_name'] = value[0]
                dishes['quantity'] = int(value[1])
                dishes['measure'] = value[2]
                cook_book[keys.strip()].append(dishes)
            empty_line = f.readline()
        #print(cook_book)
        return cook_book

#get_cook_book()

def shop_list(dishes, person_count):
    shop_list = {}
    shop_list_1 = {}
    cook_book = get_cook_book()
    dishes_list = list(dishes)
    
    for dishes_list[0] in dishes_list:
        for ingredients in cook_book[dishes[0]]:
            menu = dict(ingredients)
            menu['quantity'] *= int(person_count)
            if menu['ingridient_name'] not in shop_list:
                shop_list[menu['ingridient_name']] = {'measure': menu['measure'], 'quantity': menu['quantity']}

    for dishes_list[1] in dishes_list:
        for ingredients_1 in cook_book[dishes[1]]:
                menu_1 = dict(ingredients_1)
                if dishes_list[1] == dishes_list[0]:
                    menu_1['quantity'] *= (int(person_count)*2)
                elif dishes_list[1] != dishes_list[0]:
                    menu_1['quantity'] *= int(person_count)
                if menu_1['ingridient_name'] not in shop_list_1:
                       shop_list_1[menu_1['ingridient_name']] = {'measure': menu_1['measure'], 'quantity': menu_1['quantity']}

    shop_list_by_dises = {**shop_list, **shop_list_1}
    print(shop_list_by_dises)        
   
shop_list(['Омлет', 'Омлет'], 3)
