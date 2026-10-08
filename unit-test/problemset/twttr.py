def main():
    tweet = input('What is tweet? ')
    print(shorten(tweet))

def shorten(word):
      twt = ''

      for letter in word:
            if letter in ('aeiou') or letter in ('AEIOU'):
                  continue
            else:
                  
                  twt+=letter

      return twt



if __name__ == "__main__":
    main()