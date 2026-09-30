def convert(msg):
      msg = msg.replace(':)', '🙂')
      msg = msg.replace(':(', '🙁')
      return msg

def main():
      msg = input('')
      msg = convert(msg)
      print(msg)
main()