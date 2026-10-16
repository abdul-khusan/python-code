class Player:
      def __init__(self, name, club):
            if not name:
                  raise ValueError('Invalid Name')
            self.name = name 
            self.club = club 
      def __str__(self):
            return f'{self.name} from {self.club}'


      @property
      def club(self):
            return self._club 

      @club.setter
      def club(self, club):
            if club not in ['Barcelona', 'Real Betis', 'Real Madrid', 'Atletico Madrid', 'Sevilla']:
                  raise ValueError("Invalid house")
            self._club = club

def main():
      player = get_player()
      print(player) 
      
def get_player():
      name = input('Name: ').strip()
      club = input('Club: ').strip()
      return Player(name, club)


if __name__ == "__main__":
    main()




