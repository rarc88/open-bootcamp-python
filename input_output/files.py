# Modes
# r: read
# a: append
# w: write
# x: create

# t: texto
# b: binary

# Leer fichero completo
f = open('/etc/passwd', 'r')
data = f.read()
f.close()
print(data)

# Leer fichero linea por linea
f = open('/etc/passwd', 'r')
data = None
while data != '':
    data = f.readline()
    print(data)
f.close()

# Leer fichero como una lista
f = open('/etc/passwd', 'r')
data = f.readlines()
f.close()
print(data)
