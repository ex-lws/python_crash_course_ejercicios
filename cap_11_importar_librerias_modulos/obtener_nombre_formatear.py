from formatear_nombre import formatearNombre 

print ('Escriba q para detener el programa, de lo contrario escriba los datos solicitados')

activador =  True

while activador:

     nombres = input ('Por favor, escriba sus nombres')

     if nombres == 'q':
          activador = False

     apellido_paterno = input('Por favor, escriba su apellido paterno')

     if apellido_paterno == 'q':
          activador = False

     apellido_materno = input ('Por favor, escriba su apellido materno')

     if apellido_materno == 'q':
          activador = False

     nombre_formateado = formatearNombre (nombres, apellido_paterno, apellido_materno)
     print ('Nombre formateado:' + '\n' + nombre_formateado)

