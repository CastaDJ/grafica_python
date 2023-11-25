import random

num = 0

def num_aleatorio():

  num_ale = 100
  return random.randrange(1, num_ale)

result = num_aleatorio() 
print(result)

print(num)
