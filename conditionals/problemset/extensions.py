file = input('File name: ')

if file.endswith('.gif'):
      print('image/gif')
elif file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.png'):
      print('image/jpeg')

elif file.endswith('.pdf') or file.endswith('.txt') or file.endswith('.zip'):
      print('image/file')

else:
      print('application/octet-stream')


