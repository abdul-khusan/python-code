def main():
      while True:
            try:
                  available_fuel = input('Fraction: ')
                  fraction_fuel = get_fraction(available_fuel)

                  if (fraction_fuel == 'E'):
                        print(fraction_fuel)
                  elif (fraction_fuel == 'F'):
                        print(fraction_fuel)
                  elif (fraction_fuel == None):
                        print('None')
                  else:
                        print(f'{fraction_fuel}%')
                  break
            except (ValueError):
                  pass

def get_fraction(fraction):
     
      fraction_fuel = fraction.split('/')
      x = int(fraction_fuel[0])
      y = int(fraction_fuel[1])

      if x >= 0 and y > 0 and x<=y:
            z = (round((x / y) * 100))
            if (z <= 1):
                  return 'E'
            elif (z >=99):
                  return 'F'
            else:
                  return z
        

main()