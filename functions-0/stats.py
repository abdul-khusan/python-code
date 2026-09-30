def stats(goals, assists):
      print(str(goals + assists) + " G/A")
      return goals + assists

def main():
      player0 = stats(11, 3)
      player1 = stats(7, 6)
      player2 = stats(6, 3)
      total_ga = player0 + player1 + player2
      print(str(total_ga) + " total G/A stats of players")

main()