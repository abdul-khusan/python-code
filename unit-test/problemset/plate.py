def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) <= 6 and len(s) >= 2:
        if s[0].isalpha() and s[1].isalpha() and s.isalnum():
                    for i, letter in enumerate(s):
                        if letter.isnumeric():
                              if letter == "0":
                                    return False
                              if not s[i:].isnumeric():
                                    return False
                              
                              return True

                    return True
        else:
             return False
       
                        
    else:
      return False


if __name__ == "__main__":
    main()