paises= [
    {  
        "Nombre":"Veneuela",
        "Capital": "Caracas",
        "Peso": "Bolivariano",
        "Poblacion":
        {
            "censo": 26,
            "densidad": 28
        },
        "ciudades": {
            "Maracaibo",
            "Valencia",
            "Barquismeto",
            
        },
        "superficie": 
            {
            "total": 916
            }
            
    },
    {   
        "Nombre": "Colombia",
        "Capital": "Bogota",
        "Peso": "colombianos",
        "Poblacion":
        {
            "censo": 53,
            "densidad": 56
        },
        "Ciudades":
            {
            "Cali",
            "Barranquilla",
            "Medellin",
            "Caqueta"
            }, 
            "superficie": 
                {
                    "total": 141
                }
    },
    {  
        "Nombre": "Brasil",
        "Capital": "Brasilia",
        "Peso": "Real",
        "Poblacion":
        {
            "censo": 203,
            "densidad": 205
        },
        "Ciudades":
            {
            "brasilia",
            "sao paulo", 
            "salvador de bahia",
            "natal"   
            },
            "superficie":
                {
                    "total": 8.515
                }
    }
    ]
#recorrer todos los paises:
print("recorrer todos los paises ")
for pais in paises: 
    print("cuidades principales:")
    for cuidad in pais ["Capital"]:
        print("-" , "Capital")

for pais in paises:
    print("nombre: ", pais["Nombre"])
    print("capital: ", pais["Capital"])
    print("Poblacion: ")
    print(" Censo",
        pais["Poblacion"]["censo"],
        "millones")
    print("- Densidad",
            pais["Poblacion"]["densidad"],
            "por km2")
    print("- superfici",
            pais["superficie"]["total"],
            "yap")
    print("----------")