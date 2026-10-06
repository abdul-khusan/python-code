menu = {

    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_order = int()

while True:
      try:
            order = input('Item: ').lower()

            for item in menu:
                  item_lower = item.lower()
            
                  if order == item.lower():

                        meal = menu.get(item)
                        total_order += meal
                        print(f"${total_order:.2f}")
                        
                  else:
                        continue
            
      except EOFError:
            print(f'\nTotal: ${total_order:.2f}')
            break










