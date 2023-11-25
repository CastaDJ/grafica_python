import utils as util
import random
import data_csv
import charts

def run():

  data = data_csv.read_csv('./project/world_population.csv')
  country = input('Ingrese el pais: ')
  result = util.poppulatio_country(data, country.capitalize())
  if len(result) > 0:
    #country_ = result
    print(result[0])
    labels, values = util.get_population(result[0])
    print('labels =>',labels, 'values =>', values)
    charts.generate_graph(labels, values)
    
if __name__ == '__main__':
  run()
