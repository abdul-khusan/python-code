import sys 

# if len(sys.argv) < 2:
#       sys.exit('Too few arguments')
# elif len(sys.argv) > 2:
#       sys.exit('Too many arguments')
# print('hello, this is', sys.argv[1])


# slice 
if len(sys.argv) < 2:
      sys.exit('Too few arguments')

for arg in sys.argv[1:]:
      print('My name is', arg)