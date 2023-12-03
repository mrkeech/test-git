# cars = ['audi', 'ferrari', 'ford focus', 'toyota sienna hybrid']
# groceries = ['apples', 'oranges', 'bananas']

# def car_adder(thing_to_add, target_list):
#     if thing_to_add[0].lower() in 'abcdefg':
#         print("This car starts with A-G")
#         target_list.append(thing_to_add)
#     else:
#         print("This car starts with H-Z and we aren't allowing it in our club")
   

# car_adder('BMW', cars)
# car_adder('Honda', cars)
# car_adder('cinnamon', groceries)
# car_adder('apples', groceries)

# print(cars)
# print(groceries)

def addTwo(num):
    return num + 2

def addThree(num):
    return num + 3

print(addThree(addTwo(5)))

def namePrinter(first, last, middle=''):
    return f"The name's {last}, {first} {middle} {last}."

# print(namePrinter("James", "Bond", "Freddy"))

def giveMeMySports(name_to_add):
    sports_dict = {'soccer': ['Manchester City', 'Liverpool', 'Bayern Munich'],
                    'basketball': 'Cavaliers',
                    'Baseball': 'marlins'}
    sports_dict['wrestling'] = name_to_add
    return sports_dict

print(giveMeMySports(['Dan Gable', 'The Rock', 'The Undertaker']))