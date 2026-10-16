from datetime import date
import re
import inflect 
import sys

def main():
    print(minutes_lived(input('Birthday: ')))


def minutes_lived(birth_day):
      today = date.today()
      matches = re.search(r'^\d{4}-\d{2}-\d{2}$', birth_day)
      english_func = inflect.engine()


      if matches:
            try:
                 birthday = date.fromisoformat(birth_day)
            except ValueError:
                 sys.exit('Invalid Date')
            if birthday > today:
                 sys.exit('Invalid Date')
            else:
                  birth_diff = today - birthday
                  minute_converted = ((birth_diff.days) * 24 * 60)
                  english_word = english_func.number_to_words(minute_converted, andword="")
                  return f"{english_word.capitalize()} minutes"
      else:
            sys.exit("Invalid Date")
      

if __name__ == "__main__":
    main()