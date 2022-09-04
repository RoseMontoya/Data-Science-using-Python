#Part One
list_of_names = ['Kurt', 'David', 'Katherine']

for name in list_of_names:
    print("Where is " + name + " today?")

#Part Two
my_favorite_cars = ['Prius', 'Audi', 'Tesla']
my_favorite_flowers = ['Hibiscus', 'Tulip', 'Snapdragon', 'Lily']
my_favorite_animals = ['Dog', 'Fox', 'Octopus', 'Cat', 'Giraffe']

my_favorite_things = my_favorite_cars + my_favorite_flowers + my_favorite_animals

for thing in my_favorite_things:
    if len(thing) % 2 == 0:
        print(thing)
    else:
        continue

#Part Three
number_range = range(1, 21)

for a_number in number_range:
    if a_number % 3 ==0 and a_number % 5 ==0:
        print('ZipZap')
    elif a_number % 3 ==0:
        print('Zip')
    elif a_number % 5 == 0:
        print('Zap')
    else:
        print(a_number)




