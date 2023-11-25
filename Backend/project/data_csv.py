#se importa la libreria
from collections.abc import Iterable
import csv

def read_csv(path):
  #se abre el achivo csv y se le da permiso de read
  with open(path, 'r') as csv_file:
    #se lee el archivo csv y se delimita por ,
    reader = csv.reader(csv_file, delimiter=',')

    #se crea una list
    data = []
    #se saca las key para el diccionario
    header = next(reader);
    for row in reader:
      #se unen dos listas para crear una lista con tuplas donde se utilizara la cabeceras con la informacion
      iterable = zip(header, row)
      # se genera el diccionario
      country_dict = {key:value for key, value in iterable}

      #se grega el dict a list
      data.append(country_dict)
    #se regresa la list
  return data

if __name__ == '__main__':
  dta  = read_csv('./project/world_population.csv')

  print(dta)