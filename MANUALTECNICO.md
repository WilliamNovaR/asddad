# Manual Técnico

## Entradas Y Salidas
### Entradas
	* Usuario -> sesion.py -> funcion : crear_cuenta -> tipo str
	* Contraseña -> sesion.py -> funcion : crear_cuenta -> tipo str
	* Tipo de cuenta -> -> sesion.py -> funcion : crear_cuenta -> tipo str
	* Usuario -> sesion.py -> funcion : iniciar_sesion -> tipo str
	* Contraseña -> sesion.py -> funcion : iniciar_sesion -> tipo str
	* Id estudiante -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Periodo de evaluacion -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Autor -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Tipo trabajo -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Nombre trabajo -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Nombre director -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Nombre coodirector InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* jurado1 InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* jurado2 InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Numero de acta InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo int
	* Notas criterios jurado 1 -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo float
	* Notas criterios jurado 2 -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo float
	* Comentarios de cada criterio -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo str
	* Comentario final -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo str
	* Correciones -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo str
	* Identificador criterio -> ConfigurarCriterios.py -> funcion :  agregar_criterio, editar_criterio -> tipo str
	* Descripcion criterio -> ConfigurarCriterios.py -> funcion :  agregar_criterio, editar_criterio -> tipo str
	* porcentaje pondetacion -> ConfigurarCriterios.py -> funciones :  agregar_criterio, editar_criterio -> tipo str
### Salidas
	*pdf de acta -> CrearActa.py -> funcion : crearActa -> .pdf
	*Grafica con la ota de los estudiantes -> AnaliticaDatos.py -> funcion : grafica_notas -> tipo grafica
	*Grafica promedio de notas criterios -> AnaliticaDatos.py -> funcion : grifica_criterios -> tipo grafica
	*Datos recolectados para el acta -> InformacionActas.py, Evaluar.py -> funciones: 1. listar_actas, 2.editar_calificacion, listar_evaluacion.
	*Datos recolectados criterios -> ConfigurarCriterios.py -> funciones: editar_criterio, eliminar_criterio 





## Principales Clases

### Accionescontroller.py
	Esta clase es la engarga de guardar dentro de arreglos las acciones e incono de las acciones que tendra disponible
	cada uno de los menus laterales dependiendo del rol de la cuenta que ingrese

### ActaControlle.py 
	En esta clase se guardan dentro de un arreglo todas las actas que se generen esto con la finalidad de tener un registro de las actas
	y poder ver el historico de estas

### CriterioController.py
	En esta clase se guardan dentro de un arreglo todos los criterioes para guardarlas, recorrelas y acceder a estas de una manera ordena y rapida

### CuentaController.py 
	En este clase se guardan dentro de un arreglo todas las cuentas que se crean para guardarlas, recorrelas y acceder a estas de una manera ordena y rapida

### EvalController.py
	En este clase se guardan dentro de un arreglo todas las evaluaciones que se crean para guardarlas, recorrelas y acceder a estas de una manera ordena y rapida

### Acta.py
	Esta clase es la encarga de generar las actas en pdf con los respectivos datos establecidos para esta.

### Calificacion.py
	Esta es la clase de las notas donde se guardan todos los datos ingresados por el usuario en el fronted referente a las notas ademas posee funcionalidades para calcular las notas.

### Criterio.py
	Esta clase es donde se establcen todo los datos ingresados por el usuario en el fronted referentes a los criterios para que estos se puedan crear o modificar.

### Cuenta.py
	Esta clase es donde se establcen todo los datos ingresados por el usuario en el fronted referentes a los usuarios para que estos se puedan crear o modificar.

### EvalEstudiantes.py
	esta clase es donde se establcen todo los datos ingresados por el usuario en el fronted referentes a las evaluaciones para que estos se puedan crear o modificar ademas hay funcionalidades para calcular las notas.

## Librerias
	-fpdf = 1.7.2
	-openpyxl
	-streamlit>=1.8.1
	-streamlit-option-menu>=0.3.2
	-pydataxm == 0.2.6
	-Pillow~=9.1.0
	-DateTime~=4.4
	-matplotlib~=3.5.2



