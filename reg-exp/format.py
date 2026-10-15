import re 

model = input('Car: ').strip()


if matches := re.search(r'^(\w+), *(\w+)$', model): 
     name = matches.group(2) + ' from ' + matches.group(1)
print(f'It is {name}')