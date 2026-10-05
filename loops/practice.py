# while True:
#       n = int(input('What is n? '))
#       if n > 0:
#             break 

# for _ in range(n):
#       print('Hello')


#players 
# players = ['Leo Messi', 'Lamine', 'Pedri']
# for player in players:
#       print(player)


#dict 
players = [

      {'name': 'Lamine', 'club': 'Barcelona', 'position': 'LW'}, 
      {'name': 'Morgan Rogers', 'club': 'Chelsea', 'position': 'CAM'}, 
      {'name': 'Barella', 'club': 'Inter', 'position': 'CM'},

]
for player in players:
      print(player['name'], player['club'], player['position'], sep=', ')


