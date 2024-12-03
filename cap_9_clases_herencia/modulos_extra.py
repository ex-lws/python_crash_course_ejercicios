#Existen diferentes modulos y librerias que podemos usar en python

#Permite agrgear elementos a un diccionario como se haria con una lista...

from collections import OrderedDict

lengaujes_prgramacion_favoritos = OrderedDict()#Mantiene el orden en cómo los elementos fueron agregados.

lengaujes_prgramacion_favoritos["luis"] = "python"
lengaujes_prgramacion_favoritos["Gus"] = "C#"
lengaujes_prgramacion_favoritos["Maria"] = "Java"

for key, value in lengaujes_prgramacion_favoritos.items():

     print ("El lenguaje favorito de: " + key.title()
            + " es: " + value.title())
     

'''

Investigar acerca de modulos nos dará una mejor idea para poder trabajar con más funciones en Python

'''