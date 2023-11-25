dict = [
  {
    'name':'pantalon',
    'price' : 100
  },
  {
    'name':'camisa',
    'price' : 200
  },
  {
    'name':'zapatos',
    'price' : 300
  }
]

price = list(map(lambda x:x['price'],dict))
print(price)