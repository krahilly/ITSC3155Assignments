import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True

    while is_on:
        choice = input("What size sandwich would you like? (small/medium/large) or 'off' to quit: ").lower()
        if choice =="off":
            is_on = False
        elif choice in recipes:
            recipe = recipes[choice]
            ingredients = recipe["ingredients"]
            cost = recipe["cost"]
            if sandwich_maker_instance.check_resources(ingredients):

                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
                else:
                    print("Sorry, not enough ingredients.")
            else:
                print("Invalid choice.")


if __name__=="__main__":
    main()
