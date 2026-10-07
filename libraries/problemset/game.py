import random 
while True:
      try:
            level = int(input('Level: '))
            if level > 0:
                  break
            else:
                  continue
      except ValueError:
            continue

guess = random.randint(1, level)



while True:
      
      try:
            user_guess = int(input('Guess: '))
            if user_guess > 0:
                  if user_guess > guess:
                        print('Too large')
                        continue
                  elif user_guess < guess:
                        print('Too small')
                        continue
                  else:
                        print('Just Right')
                        break
            else:
                  continue
      except ValueError:
            continue
