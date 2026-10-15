# regex 
# .   any character except a new line                     |
# *   0 or more repetitions                     |
# +   1 or more repetitions                     |
# ?   0 or 1 repetition                      |
# {m} m repetitions                     |
# {m,n} m-n repetitions                     |

# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character
# ----------------------------------------------------------------

# gmail = input('What is your email? ').strip()

# username, domain = gmail.split('@')
# if username and '.' in domain:
#       print('Valid')
# else:
#       print('Invalid')
# these are all good but insufficient. Python has built-in function for us. 

import re 
mail = input('What is your email? ').strip()
# if re.search(r'^[^@]+@[^@]+\.com$', mail) :
# if re.search(r'^w+@w+\.com$', mail):
if re.search(r'\w+@(\w+\.)?\w+\.edu$', mail):
      print('Valid')
else:
      print('Invalid')


