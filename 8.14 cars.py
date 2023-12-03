def cars(make, model, **details):
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in details.items():
        car[key] = value
        return car
    
audi_r8 = cars('audi', 'r8',
               seats= 'leather',
               engine= 'v10')
print(audi_r8)