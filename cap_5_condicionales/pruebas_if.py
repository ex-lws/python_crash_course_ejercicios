#Las pruebas if son basicamente condicones

autos = ['audi', 'bmw', 
         'subaru', 'toyota']

#Si algun elemento llega a ser bmw, caambialo a mayusculas e imprimelo

#Una condicional if, es basciamente una comparacion True or False

for auto in autos:

    if auto == 'bmw': #True, pero si fuera if auto == 'lotus':, entonces seria False  

        print (auto.upper()) #Como es True, entonces entra a la identacion del if

    else: #Significa, si ya acabo el if, entonces siguie tu curso normal del programa

        print (auto.title()) #Lo que hace el programa al terminar o no cumplirse la condicion

#El operador = se utiliza comunmente para asignar y renombrar variables

#El operador !=- es diferente de, quiere decir, si el elemento es distinto de, enotnces...

toppings_helado = 'chispas de chocolate' #Definimos el sabor que queremos

if toppings_helado != 'jarabe de chocolate': #Si es sabor definidor es diferente al sabor estandar, mandar un recordatorio, usamos el operador !=

    print ('No te olvides del jarabre de chocolate')

#A los simbolos utilizados en las diferentes comparacioes con if, se les llama operadores de igualacion o igualdad.

edad = 17

if edad == 18: #Igual y solo igual que...
    print ('mayor de edad')

if edad != 18: #Diferente de...
    print ('menor de edad')

#Tenemos otros operadores usados en las pruebas de condicion, llamados mayor que, menor que

#MENOR QUE O MENOR O IGUAL QUE = <, <=

#mmAYOR QUE O MAYOR O IGUAL QUE = >, >=

salario = 1000

if salario < 1200:
    print ('Salario estandar')

if salario <= 1200:
    print ('salario plus')

if salario >= 1200:
    print ('Salario extra')

