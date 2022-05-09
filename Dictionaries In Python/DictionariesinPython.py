#Part One
#Create Dictionaries about pet information
Gingko = {'Type' : 'Dog', 'Color' : 'Black and White', 'Nickname' : 'Gingky-Binks', 'Owner' : 'Gabby and Rose'}
Ollie = {'Type' : 'Dog', 'Color' : 'Golden', 'Nickname' : 'Pie-pie', 'Owner' : 'Chantal and Ace'}

#Iterate over each dictionary, printing each key-value pair. 
for key, value in Gingko.items():
    print(key, ": ",value)
for key, value in Ollie.items():
    print(key, ": ",value)
       
#Part Two
#Dictionary Creation
china = {'Capital': 'Beijing'}
costa_rica = {'Capital': 'San Jose'}
japan = {'Capital': 'Tokyo'}
england = {'Capital': 'London'}
france = {'Capital': 'Paris'}
belgium = {'Capital': 'Brussels'}

#Adding Info
china.update({'Population': '1.402 billion', 'Interesting Fact': 'China has the largest population in the world.', 'Language': 'Mandarin'})
costa_rica.update({'Population': '5.09 million', 'Interesting Fact': 'Costa Rica is one of the happiest countries in the world.', 'Language': 'Spanish'})
japan.update({'Population': '125.8 million', 'Interesting Fact': 'There is 1 vending machine for every 25 people.', 'Language': 'Japanese'})
england.update({'Population': '53.01 million', 'Interesting Fact': 'England is one of four nations that make up the UK.', 'Language': 'English'})
france.update({'Population': '66.9 million', 'Interesting Fact': 'The French eat 25,000 tons of snails each year.', 'Language': 'French'})
belgium.update({'Population': '11.35 million', 'Interesting Fact': 'Belgium holds the world record for the longest period without a government.', 'Language': 'Dutch, French, and German'})

#Printing key value pairs
for key, value in china.items():
    print(key, ": ", value)
for key, value in costa_rica.items():
    print(key, ": ", value)
for key, value in japan.items():
    print(key, ": ", value)
for key, value in england.items():
    print(key, ": ", value)
for key, value in france.items():
    print(key, ": ", value)
for key, value in belgium.items():
    print(key, ": ", value)
    
#Part Three
#Dictionary of Pizza Order
pizza_order = {
    "Customer's Name" : 'Andrew', 
    'Size' : 'small', 
    'Crust Type' : 'thin-crust', 
    'Toppings' : {
        'topping1' : 'extra cheese', 
        'topping2' : 'sausage', 
        'topping3' : 'bacon'}
    }
#Printing Order
print("Thank you for your order, ", pizza_order.get("Customer's Name"),"."
" You have ordered a", pizza_order.get('Size'), ", " 
, pizza_order.get('Crust Type'), " pizza with the following toppings: ",
(pizza_order['Toppings']['topping1']), ", ",
(pizza_order['Toppings']['topping2']), ", ",
(pizza_order['Toppings']['topping3']), ".")