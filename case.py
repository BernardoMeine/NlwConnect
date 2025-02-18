class MyClass:
  def __enter__(self):
    print('Entering!!!')

  def __exit__(self, exc_type, exc_value, exc_tb):
    print('Exiting!!!')

with MyClass() as mc:
  print('Inside the block')
  raise Exception('This is an exception')