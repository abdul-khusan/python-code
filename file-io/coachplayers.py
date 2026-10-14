
import csv
# coachplayers = []

# with open('coachplayers.csv', 'r') as file:
#       for line in file:
#             name, club = line.rstrip().split(',')
#             coachplayers.append({'name': name, 'club': club})

# def get_name(coachplayer):
#       return coachplayer['name']


# for coachplayer in sorted(coachplayers, key=lambda coachplayer: coachplayer['name']):
#       print(f'{coachplayer['name']} is in {coachplayer['club']}')



coachplayers = []

with open('coachplayers.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:
            coachplayers.append({'name': row[0], 'club': row[1]})

for coachplayer in sorted(coachplayers, key=lambda coachplayer: coachplayer['name']):
      print(f'{coachplayer['name']} is in {coachplayer['club']}')