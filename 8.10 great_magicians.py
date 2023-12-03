magician_names = ['waldo','norris','bumbsy']

def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name)



def make_great(magician_names):
    while magician_names:
        current_magician = magician_names.pop()
        print("The Great " + current_magician.title())

make_great(magician_names)
show_magicians()