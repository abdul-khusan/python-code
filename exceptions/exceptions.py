
# try and except lets us test user input before something goes wrong. 
# try:
#       x = int(input('What is X? '))
#       print(f'x is {x}')
# except ValueError:
#       print('x is not integer')


# user get prompt repeatedly unless they enter the integer
# while True:
#       try:
#             x = int(input('What is X? '))
#       except ValueError:
#             print('X is not integere')
#       else:
#             break
# print(f'x is {x}')


# we can turn this into function
# def main():
#       x = get_int()
#       print(f"x is {x}")

# def get_int():
#       while True:
#             try:
#                   x = int(input('What is X? '))
#             except ValueError:
#                   print('X is not integer')
#             else:
#                   return x
      

# main()


# pass
def main():
      x = get_int('What is X? ')
      print(f'X is {x}')

def get_int(prompt):
      while True:
            try:
                  return int(input(prompt))
            except ValueError:
                  pass

main()


