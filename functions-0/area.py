def area(length, width):
      print(str(length * width) + " square feet")
      return length * width


def main():
      house = area(73, 28)
      yard = area(73, 57)
      total = house+yard
      print(str(total) + " total square feet")
main()