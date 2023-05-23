#dá o total somado dos varios items

import atexit

menu={    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00 }

total=0

while True:
    print("Item:", end=" ")
    try:
        item = input()
        item=item.strip().lower()
        item=item.title()
        if item in menu:
            total=menu[item] + total
            print(f"Total:${total:.2f}")

        
    except EOFError:   #usar contrlo-z-enter
              break

