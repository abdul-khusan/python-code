playstyle = input('Attacking or Defensive? ')
tactic = input('Horizontal or Vertical?  ')

def main():
      if playstyle == 'Attacking':
            if tactic == 'Horizontal':
                  recommend('Pep Guardiola')
            else:
                  recommend('Jurgen Klopp')
                  
      else:
            if tactic == 'Horizontal':
                  recommend('Diego Simeone')
            else:
                  recommend('Jose Mourinho')


def recommend(game):
      print("You might like", game)


main()