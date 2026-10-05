prompt = input('camelCase: ')
lowercase = ''

for letter in prompt:
      if letter.isupper():
            letter = f"_{letter.lower()}"
            lowercase +=letter
      else:
            lowercase+=letter

print(lowercase)