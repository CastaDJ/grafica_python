#Set union
print('UNION')
set_a = {'col', 'bol', 'per'}
set_b = {'arg', 'bol', 'col'}
set_c = set_a.union(set_b)
print(set_c)
# union con operadores aritmeticos
print('UNION CON OPERADORES')
print(set_a | set_b)

#Set intersection
print('INTERSECTION')
set_a = {'col', 'bol', 'per'}
set_b = {'arg', 'bol', 'col'}
set_c = set_a.intersection(set_b)
print(set_c)
# intersection con operadores aritmeticos
print('INTERSECTION CON OPERADORES')
print(set_a & set_b)

#Set difference
print('DIFFERENCE')
set_a = {'col', 'bol', 'per'}
set_b = {'arg', 'bol', 'col'}
set_c = set_a.difference(set_b)
print(set_c)
# difference con operadores aritmeticos
print('DIFFERENCE CON OPERADORES')
print(set_a - set_b)

#Set symmetric difference
print('SYMMETRIC DIFFERENCE')
set_a = {'col', 'bol', 'per'}
set_b = {'arg', 'bol', 'col'}
set_c = set_a.symmetric_difference(set_b)
print(set_c)
# symmetric difference con operadores aritmeticos
print('SYMMETRIC DIFFERENCE CON OPERADORES')
print(set_a ^ set_b)