#libreria para graficos
import matplotlib.pyplot as plt

#se crea function
def generate_graph(lavel, values):
  fig, ax = plt.subplots()
  ax.bar(lavel, values)
  plt.show()


if __name__ == '__main__':
  #se genera la lista de datos
  lave = ['a', 'b', 'c', 'd', 'e'	]
  value = [10,21,32,40,58]
  generate_graph(lave, value)
