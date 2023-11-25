'''
# Buscar el archivo para abrirlo
file = open('./text.txt')

#=====================================
# -----  READ ---
#=====================================

# leer el archivo abierto anterior mente
print(file.read())
# leer el archivo por lineas
print(file.readline())

#para cerrar el archivo
file.close()
'''

#=====================================
# -----  WRITE ---
#=====================================

# Buscar el archivo para abrirlo y darle permisos
file = open('./text.txt', 'r+')

for doc in file:
  file.write('\n nuevo mundo\n')