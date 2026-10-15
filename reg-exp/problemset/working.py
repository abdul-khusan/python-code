import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
      matches = re.search(r'^(\d+)(?::(\d+))?\s(AM|PM)\sto\s(\d+)(?::(\d+))?\s(AM|PM)$', s)

      if matches:
            first_hour = int(matches.group(1))
            first_minute = int(matches.group(2) or 0)
            first_time = matches.group(3)
            second_hour = int(matches.group(4))
            second_minute = int(matches.group(5) or 0)
            second_time = matches.group(6)


      
            if 1 <= first_hour <= 12 and 0 <= first_minute <=59 and 1 <= second_hour <= 12 and 0 <= second_minute <=59:
            
                  if first_time == 'PM' and first_hour !=12:
                        first_hour = (first_hour + 12)
                  
                  if second_time == 'PM' and second_hour !=12:
                        second_hour = second_hour + 12

                  if first_time == 'AM' and first_hour == 12:
                        first_hour = 0
                  if second_time == 'AM' and second_hour == 12:
                        second_hour = 0
                  return f'{first_hour:02}:{first_minute:02} to {second_hour:02}:{second_minute:02}'
                  
            else:
                  raise ValueError

      else:
            raise ValueError





if __name__ == "__main__":
    main()


