def sandwhich(*toppings):
    print("This sandwhich will have:")
    for topping in toppings:
        print('-' + topping)

sandwhich('mushrooms')
sandwhich('mushrooms, cheese, ham')
sandwhich('peppers', 'ham', 'salami')