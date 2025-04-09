# Diccionario 
# Es una estructura o una coleccion de datos que 
# los almacena  en pares 
# clave-valor 
# -Un diccrionario comienza y termian con llaves 
# (curly y braces )
# y la clave se separa del valor por dos (:)
# y lo mismo cada elemento o propiedad del 
# diccionario  se separa por una coma 

# ejemlo: diccionario 
# que almacene los datos de un 
# pais 

pais1 = {
            'nombre': 'Colombia',
            'capital': 'Bogota',
            'moneda': 'peso colombiano',
            'ciudades': [
                        "cordoba",
                        "choco", 
                        "cali"
                        "medellin"
                        ],
            'poblacion': { 
                'censo': 53,
                'densidad': 46,
                
                        }
        } 



pais2 = {
            'nombre': 'Brasil',
            'capital': 'rio de janeiro',
            'moneda': 'peso brasileño',
            'ciudades': [
                        "brasilia",
                        "sao paulo", 
                        "salvador de bahia",
                        "natal"
                        ],
            'poblacion': { 
                'censo': 203,
                'densidad': 205,
                
                        }
        }

pais3 = {
            'nombre': ' España',
            'capital': 'madrid',
            'moneda': 'peso español',
            'ciudades': [
                        "barcelon",
                        "sevilla", 
                        "valencia",
                        "ceuta"
                        ],
            'poblacion': { 
                'censo': 49,
                'densidad': 97,
                
                        }
        }

#acceder a la informacion del pais 
print (pais1['nombre'])
print (pais2['capital'])
#acceder a una cuidad del pais 
print(pais3['ciudades'][2])
print("------------")

#iterar las ciudades del pais

for ciudad in pais1['ciudades']:
    print(ciudad)


for ciudad in pais2['ciudades']:
    print(ciudad)

for ciudad in pais3['ciudades']:
    print(ciudad)

#acceder dato poblacionales 

print("---------")

print("Censo:", 
    pais1['poblacion']['censo'], 
    "millones de habitantes")

print("Dencidad:", 
    pais1['poblacion']['densidad'], 
    "por km2")