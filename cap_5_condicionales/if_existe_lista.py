#Podemos utilziar if para comprobar si algun elemento se encuentra en la lista o bien en una tupla

#Estos son in, si un elemento esta en...

#Y not in, si un elemento no esta en...


lista_usuarios = ['supervisor', 'quimico', 'disenador', 'recursos humanos'] 
#Definimos una lista con varios elementos dentro

#Para saber si un elemento esta en la lista, entonces...

#colocamos el if, variable in lista.

#in = dentro de

if 'quimico' in lista_usuarios: #Usando in
    print ('EL EMPLEO DE QUIMICO YA ESTA CUBIERTO')

#Colocamos if, elemento lista, not in, lista: 

#not in = no dentro de

if 'marketing' not in lista_usuarios: #Usando not in
    print ('El empleo de marketing no esta en ocupacion')
