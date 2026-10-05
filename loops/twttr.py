tweet = input('Input: ').lower()
twt = ''

for letter in tweet:
      if letter in ('aeiou') or letter.isspace():
            continue
      else:
            
            twt+=letter

print(twt)
