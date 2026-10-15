import re



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    matches = re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip)
    if matches:
            first = int(matches.group(1))
            second = int(matches.group(2))
            third = int(matches.group(3))
            fourth = int(matches.group(4))

            if first >= 0 and first <= 255 and second >= 0 and second <= 255 and third >= 0 and third <= 255 and fourth >= 0 and fourth <= 255:
                        return True

            else:
                  return False
    else:
      return False




if __name__ == "__main__":
    main()





