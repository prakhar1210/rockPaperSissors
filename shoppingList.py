shopping_list = []

def start_menu():
    print("\n what do you want to add in the cart??")
    print("""
            ENTER "Done" to stop adding items.
            Enter "Help" for additional information.
            Enter "Show" to see your shooping list.
            Enter "Remove" to remove an item from your shopping list.
          ----------------------------------------------------------------
          """)
    

def add_items_to_list(item):
    item = item.capitalize()

    if item not in shopping_list:
        shopping_list.append(item)
        print("{} is added to your shopping list.".format(item))
        print("{} You have these items in your shopping list.".format(len(shopping_list)))
    else:
        print("You already have that item on your list!!!")


def remove_items_from_list(item):
    item = item.capitalize()

    if item in shopping_list:
        shopping_list.remove(item)
        print("{} is removed from your cart.".format(item))
        print("You have {} these items in your shopping cart.".format(len(shopping_list)))
    else:
        print("You donot have this item in your list!!!")


def print_the_cart_items():
    print("Items in the Cart")
    for items in shopping_list:
        print(items)



start_menu()
while True:
    user_input = input(">")

    if user_input == "Done":
        start_menu()
        break

    elif user_input == "Help":
        start_menu()
        print("""
                Type in an item into the box provided to you
                add an item to your shopping cart.
            """)        
        continue
    

    elif user_input == 'Show':
        start_menu()
        print_the_cart_items()
        continue
    
    
    elif user_input == "Remove":
        print_the_cart_items()
        item = input("What do you want to remove?: ")
        start_menu()
        remove_items_from_list(item)
        continue

    else:
        start_menu()
        add_items_to_list(user_input)    

print_the_cart_items()    
