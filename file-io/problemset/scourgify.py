import csv
import sys

new_csv = []
try:
      if len(sys.argv) > 3:
            sys.exit('Too many arguments')
      elif len(sys.argv) < 3:
            sys.exit('Too few arguments')
      else:
            with open(sys.argv[1], 'r') as file:
                  reader = csv.DictReader(file)
                  for row in reader:
                        full_name = row["name"]
                        house = row['house']
                        last,name = full_name.split(",")
                        name = name.strip()

                        new_csv.append({'last':last, 'first':name, 'house':house})


            with open(sys.argv[2], 'w') as file:
                  writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
                  writer.writeheader()
                  for line in new_csv:
                        writer.writerow(line)

except FileNotFoundError:
      sys.exit('File not found')




