# 2022-1 Proyecto Final POO
> Lenguaje Usado -> Python 3.10

## Integrantes:
> * William Andres Nova Rojas (8956350).

## Presentación:
Este proyecto es un programa de interfaz web usando python y streamlit en el que se usan los diversos conseptos vistos en el curso de POO
El objetivo de este proyecto era generar un software para la calificacion de trabajos finales de maestria.


## Enunciado:
La dirección de los posgrados en ingeniería de software de la Pontificia Universidad Javeriana Cali quiere hacer un
sistema de información que facilite la calificación de los trabajos de grado de maestría cuando los estudiantes realizan
su sustentación pública. La directora espera que el sistema entregue un archivo de texto con los resultados de la
calificación obtenida por el estudiante y los comentarios relacionados con la evaluación. Esta evaluación se registra
en un acta de evaluación que es diligenciada luego de la sustentación por los dos jurados participantes y está
compuesta por:
* Número, fecha, autor, nombre del trabajo, tipo de trabajo ( 1. Aplicado, 2. Investigación ), director,
codirector (algunas veces existe un codirector), jurado 1, jurado 2.
* Criterios de evaluación. Actualmente son 8 criterios de evaluación pero podrían extenderse en el futuro.
Cada criterio tiene un identificador, un texto que es el texto que se presenta a los evaluadores y un
porcentaje de ponderación. El porcentaje de ponderación está definido por la dirección de los posgrados.
Eventualmente podría ser ajustados por la dirección de los posgrados.
* En el acta para cada criterio de evaluación se incluye la calificación del jurado número 1 y la calificación del
jurado número dos y los comentarios específicos para el criterio.
* El acta permite incluir observaciones adicionales y comentarios específicos sobre las condiciones para la
aprobación del trabajo final

## Principales Funcionalidades:
En este software el principal objetivo es el facilitar el proceso de calificacion y creacion de actas de un grado, el cual dependiendo el rol del usuario
tendrá disponibilidad de diversas funcionalidades estas son las funcionalidades:
> Roles y Funcionalidades:
* Asistente -> Inicializar Acta de Evaluación, ver actas creadas y estadisticas de notas.
* Jurado -> Calificar, Exportar acta, editar calificacion y ver calificaciones realizadas y estadisticas de notas
* Director@ -> Director/a -> Modificar los criterios de calificacion y ver las actas creadas y estadisticas de notas.

### Fecha De entrega: 11:55 pm del 21 de mayo del 2022.
