import sys 



name_length = len(sys.argv)
try:
      if name_length == 2:
            name = sys.argv[1]
            if name.endswith('.py'):
                  lines = []
                  with open(name, 'r') as file:
                        for line in file:
                              if line.lstrip().startswith('#') or line.strip() == "":
                                    continue
                              else:
                                    line_name = line.rstrip()
                                    lines.append(line_name)
            else:
                  sys.exit('File is not python file')

            print(len(lines))
      elif name_length > 2:
            sys.exit('Too many arguments')
      elif name_length < 2: 
            sys.exit('Too few arguments')

      
except FileNotFoundError:
      sys.exit('File not found')



# first we need to receive sys.argv
# second, we need to read that file and tell the number of lines 
# third, we need to output 
# then we can check for python, etc. 