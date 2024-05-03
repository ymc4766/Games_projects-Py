MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    # true when order made or False when ingredient unsifficient
    # is_enough = True
    for  item in order_ingredients :
       if order_ingredients[item] >= resources[item] :
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def  process_coins():
    # return total calculated  coins inserted
    print('please insert Coins ')
    total =  int(input('how many quarters? : ')) * 0.25
    total +=  int(input('how many dimes? : ')) * 0.1
    total +=  int(input('how many nickles? : ')) * 0.05
    total +=  int(input('how many pennies? : ')) * 0.01
    return total

def is_transaction_succesfull  (money_received , drink_cost) :

    # return true when payment accepted  or false is unsifficient \
    if money_received >= drink_cost :
        change = round(money_received - drink_cost ,2)
        print(f'here is your change , ${change}')
        global profit
        profit +-drink_cost
        return True
    else :
        print('sorry not enough money :) funded ...')
        return False

def make_coffee(drink_name , order_ingredients) :
    # deduct order ingredient from resources

    for item in order_ingredients :
        resources[item] -=order_ingredients[item]
    print(f'here is your drink {drink_name} :)')


is_on = True

while is_on :
    choice = input('what would you like /espereso/cappucino/latte ')
    if choice == 'off':
        is_on = False
    elif choice == 'report' :
        print(f"water : {resources['water']} 100ml")
        print(f"milk : {resources ['milk']} 50ml")
        print(f"coffee : {resources ['coffee']} 22ml")
        print(f"Money: ${profit}")

    else :
        drink = MENU[choice]
        # print(drink)
        if is_resource_sufficient(drink['ingredients']):
           payment = process_coins()
           if is_transaction_succesfull(payment , drink['cost']):
               make_coffee(choice  , drink['ingredients'])







      


    

    

# print(MENU.cappuccino.tolist())
