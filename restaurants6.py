# RESTAURANT COLLECTION PROGRAM

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 n:  Search for all the restaurants that serve a specified cuisine
 o:  Search for all the restaurants that serve a dish whose name contains a given word or phrase
 p:  Print all the restaurants
 c:  Change prices for the dishes served
 q:  Quit
"""

def handle_commands(diners: list) -> list:
    """ Display menu, accept and process commands.

    """
    done = False
    while not done:
        response = input(MENU)
        if response=="q":
            done = True
            return diners
        elif response=='a':
            r = restaurant_get_info()
            diners = collection_add(diners, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            diners = collection_remove_by_name(diners, n)
        elif response=='p':
            print(collection_str(diners))
            for i in diners:
                print("Average Price: ${}    Average Calories: {}".format(average_price(i), average_cal(i)))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in collection_search_by_name(diners, n):
                print(restaurant_str(r))
        elif response == 'n':
            k = input("Please enter the name of the cuisine:  ")
            restaurantsWithCuisine = []
            for o in restaurant_search_by_cuisine(diners, k):
                print(restaurant_str(o))
                restaurantsWithCuisine.append(o)
            for i in restaurantsWithCuisine:
                print("Average Price: ${}    Average Calories: {}".format(average_price(i), average_cal(i)))
        elif response == 'o':
            restaurantsWithPhrase = []
            y = input("Please enter a word or a phrase from a dish:  ", )
            for q in restaurant_search_by_phrase(diners, y):
                if q not in restaurantsWithPhrase:
                    restaurantsWithPhrase.append(q)
                    print(restaurant_str(q))
            for i in restaurantsWithPhrase:
                print("Average Price: ${}    Average Calories: {}".format(average_price(i), average_cal(i)))
        elif response=='c':
            n = float(input("Please enter the amount representing a percentage change in price:  "))
            diners = collection_change_price(diners, n)
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
Dish = namedtuple('Dish', 'name price calories')
#Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', [Dish('Escargots', 23.50)])

def restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:     " + menu_display(self.menu) + "\n\n")

def restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        menu_enter())

def restaurant_change_price(r:Restaurant, number: float) -> Restaurant:
    '''takes a restaurant and changes all of its dishes prices by given amount'''
    r = r._replace(menu = menu_change_price(r.menu, number))
    return r

#### COLLECTION
# A collection is a list of restaurants

def collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def collection_str(diner_collection: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in diner_collection:
        s = s + restaurant_str(r)
    return s

def collection_search_by_name(diner_list: list, diner_name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in diner_list:
        if r.name == diner_name:
            result.append(r)
    return result

def restaurant_search_by_cuisine(diner_list:list, cuisine_name:str)->list:
    ''' Return list of Restaurants in input list whose cuisine matches input string'''
    result = []
    for r in diner_list:
        if r.cuisine == cuisine_name:
            result.append(r)
    return result

def restaurant_search_by_phrase(diner_list:list, phrase:str)->list:
    '''Return list of Restaurants in input list where the restaurant has a dish with a certain phrase'''
    result = []
    for r in diner_list:
        for k in r.menu:
            if phrase in k.name:
                result.append(r)
    return result

def collection_add(diner_list: list, diner: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    diner_list.append(diner)
    return diner_list

def collection_remove_by_name(diners: list, diner_name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in diners:
        if r.name != diner_name:
            result.append(r)
    return result

def collection_change_price(diner_list: list, number:float) -> list:
    '''takes a collection  changes prices within it and returns an updated collection'''
    updated_diners = []
    for r in diner_list:
        new = restaurant_change_price(r, number)
        updated_diners.append(new)
    return updated_diners

#Dish


def dish_str(self:Dish) -> str:
    ''' Takes a dish and returns a string in the from of name, price'''
    return ("Name: " + str(self.name) + "   Price: $" + str(self.price)) + "   " + str(self.calories)+" calories"

def dish_get_info() -> Dish:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the price of that dish:  ")),
        float(input("Please enter the calories of the dish: ")))

def dish_change_price(dish: Dish, number:float) -> Dish:
    '''takes a dish and changes is prices by given number'''
    result=0
    if(number<0):
        result = abs(dish.price*(number/100))
    elif(number==0):
        result = dish.price
    elif(number>0):
        result = dish.price+(dish.price*(number/100))
    return Dish(dish.name,result, dish.calories)


#Menu
#A list of dishes

def menu_enter()-> 'menu':
    '''repeatedly prompts user for a dish, adding it to the list of dishes until
    user ends function'''
    done = False
    menu = []
    while not done:
        prompt = input("Would you like to add a dish: Yes or No? ")
        if prompt.title() == "Yes":
            done = False
            menu.append(dish_get_info())
        else:
            done = True
            print ("Menu done.")
    return menu

def dish_raise_price(item1:Dish)->Dish:
    "Takes a dish and number and returns a dish with its price increased by a number"
    return Dish(item1.name,item1.price+2.5,item1.calories)

def menu_raise_prices(m:list)->list:
    "Takes a menu and returns a modified list with higher prices"
    result=[]
    for dish in m:
        result.append(dish_raise_price(dish))
    return result

def restaurant_raise_prices(diners:Restaurant)->Restaurant:
    "Takes a restaurant and returns a restaurant with prices raised by 2.50"
    new_prices = menu_raise_prices(diners.menu)
    return Restaurant(diners.name,diners.cuisine,diners.phone,new_prices)

def menu_display(menu:'list of Dishes')-> str:
    '''Takes a list of Dishes and returns one large string consisting of the string
       representation of each dish followed by newline('\n') character'''
    result = ''
    for dish in menu:
        result += dish_str(dish) + "\n" + "          "
    return result

def menu_change_price(menu: list, number: float) -> list:
    '''takes a list of dishes and changes their price by given'''
    new_dishlist = []
    for d in menu:
        new_dishlist.append(dish_change_price(d, number))
    return new_dishlist

def average_price(r:Restaurant)->float:
    '''takes in a list of dishes and finds the average price'''
    p = 0
    n = len(r.menu)
    for i in r.menu:
        p += float(i.price)
    return p/n

def average_cal(r:Restaurant)->float:
    '''takes in a list of dishes and finds the average calories'''
    c = 0
    n = len(r.menu)
    for i in r.menu:
        c += float(i.calories)
    return c/n

restaurants()
