import emoji 
import sys 


if len(sys.argv) < 2:
      sys.exit('Too few Arguments')
elif len(sys.argv) > 2:
      sys.exit('Too many arguments')


print(emoji.emojize(sys.argv[1]))