# names = []

# for _ in range(3):
#       name = input('What is your name? ')
#       names.append(name)

# for name in sorted(names):
#       print(f'hello {name}')


# 'a' for appending, 'w' writing from start each time
# name = input('What is your name? ')
# file = open('names.txt', 'a')
# file.write(name)
# file.close()


#with - using "with" we do not need to close the file as it closes itself 
# name = input('What is your name? ')
# with open('names.txt', 'a') as file:
#       file.write(f'{name}\n')


#read
# with open('names.txt', 'r') as file:
#       lines = file.readlines()

# for line in lines:
#       print('hello', line)


# with open('students.csv') as file:
#       for line in file:
#             row = line.rstrip().split(',')
#             print(f'{row[0]} is in {row[1]}')



students = []
with open('students.csv') as file:
      for line in file:
            name, house = line.rstrip().split(',')
            student = {'name': name, 'house': house}
            students.append(student)

for student in students:
      print(f'{student['name']} is in {student['house']}')