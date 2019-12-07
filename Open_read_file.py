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
        from collections import Counter
        shop_list = {}
        cook_book = get_cook_book()
        for dish in dishes:
            c = Counter(dishes)
            #print(c[dish])
            for ingredients in cook_book[dish]:
                menu = dict(ingredients)
                menu['quantity'] *= (int(person_count)*c[dish])
                if menu['ingridient_name'] not in shop_list:
                    shop_list[menu['ingridient_name']] = {'measure': menu['measure'], 'quantity': menu['quantity']}
        print(shop_list)
        return shop_list

shop_list(['Омлет', 'Омлет', 'Утка по-пекински'], 3) 
