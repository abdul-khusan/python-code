due = 50
change = int()

while True:
      coin_insert = int(input('Enter the coin: '))
      if coin_insert == 25 or coin_insert == 10 or coin_insert == 5:
            due -= coin_insert 
            
            if due <= 0:
                  change = (due * -1)
                  print('Change owed:', change)
                  break
            print('Amount due:', due)

      else:
            print('Amount due:', due)
            continue