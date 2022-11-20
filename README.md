# CreacionTurnos
##Aplicación en Django para creación y asignación de turnos
En esta aplicacion se plantea un gestor de turnos y pacientes, para ello se provee la base de datos con la que se realizaron las pruebas
##funcionamiento
```
Version de python: 3.10
Version de Django: 4.1.3
```
una vez instalada la base de datos, en el archivo /creacionTurnos/settings.py se encuentra la configuracion para realizar la conexion, una vez configurado, se puede iniciar la aplicación con el comando 
```
python manage.py runserver
```
##Rutas
Para administrar usuarios se puede realizar un registro en la ruta .../autenticacion/registro, o desde el administrador de Django .../admin, el cual sirve de igual manera para gestionar permisos de staff a los usuarios. La administración de los turnos se debe hacer directamente desde el administrador de Django
###Superusuario: 123456, clave: 1234
La página cuenta con autenticacion, y asi mismo no permite a un usuario no identificado acceder a las funcionalidades del miso, y unicamente se permite a los usuarios que sean staff a modificar el estado de un turno (pendiente, activo, finalizado).
##Apis
Hay una api creada para ver la información de los turnos con la ruta .../api/turnos/ en la que se muestra toda su informacion; la segunda api verifica la existencia de un usuario identificado por su cedula en la ruta .../api/usuarios/"cedula" 