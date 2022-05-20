import json
from model.EvalEstudiante import EvaluacionEstudiante
from model.Calificacion import Calificacion

class EvaluadorController:
    def __init__(self) -> None:
        super().__init__()
        self.evaluaciones = []

    def agregar_evaluacion(self, evaluacion_obj):
        self.evaluaciones.append(evaluacion_obj)

    # esta funcion sirve para guardar las evaluaciones en un .json para que cada vez que se cierra y abre el programa se guarden los parametros
    def cargar(self):
        lista = []
        # se transforma a los objetos en diccionarios para poder cargarlos en el .json
        for i in self.evaluaciones:
            diccionario = {'calificacion': [], 'id_estudiante': '', 'periodo': '', 'nombre_autor': '',
                           'nombre_trabajo': '', 'tipo_trabajo': '', 'nombre_director': '', 'nombre_codirector': '',
                           'enfasis': '', 'nombre_jurado1': '', 'nombre_jurado2': '', 'inicilizar': '', 'nota': '',
                           'comentario_final': '', 'correciones': '', 'recomendacion': ''}
            diccionario['calificacion'] = i.guardar_calificaciones()
            diccionario['id_estudiante'] = i.id_estudiante
            diccionario['periodo'] = i.periodo
            diccionario['nombre_autor'] = i.nombre_autor
            diccionario['nombre_trabajo'] = i.nombre_trabajo
            diccionario['tipo_trabajo'] = i.tipo_trabajo
            diccionario['nombre_director'] = i.nombre_director
            diccionario['nombre_codirector'] = i.nombre_codirector
            diccionario['enfasis'] = i.enfasis
            diccionario['nombre_jurado1'] = i.nombre_jurado1
            diccionario['nombre_jurado2'] = i.nombre_jurado2
            diccionario['inicilizar'] = i.inicilizar
            diccionario['nota'] = i.nota
            diccionario['comentario_final'] = i.comentario_final
            diccionario['correciones'] = i.correciones
            diccionario['recomendacion'] = i.recomendacion
            lista.append(diccionario)
        with open('data_calificaciones.json', 'w') as outfile: #se cargan los datos en data_calificaciones.json
            json.dump(lista, outfile)


    def leer(self):
        with open('data_calificaciones.json') as json_file:
            data = json.load(json_file)
            arreglo = []
            for cargar in data:
                lista = []
                evaluaciones = EvaluacionEstudiante()
                for datos in cargar['calificacion']:
                    calificacion = Calificacion()
                    calificacion.numero_jurados = datos['numero_jurados']
                    calificacion.id_criterio = datos['id_criterio']
                    calificacion.ponderacion = datos['ponderacion']
                    calificacion.nota_jurado1 = datos['nota_jurado1']
                    calificacion.nota_jurado2 = datos['nota_jurado2']
                    calificacion.nota_final = datos['nota_final']
                    calificacion.comentario = datos['comentario']
                    lista.append(calificacion)
                evaluaciones.calificacion = lista
                evaluaciones.id_estudiante = cargar['id_estudiante']
                evaluaciones.periodo = cargar['periodo']
                evaluaciones.nombre_autor = cargar['nombre_autor']
                evaluaciones.nombre_trabajo = cargar['nombre_trabajo']
                evaluaciones.tipo_trabajo = cargar['tipo_trabajo']
                evaluaciones.nombre_director = cargar['nombre_director']
                evaluaciones.nombre_codirector = cargar['nombre_codirector']
                evaluaciones.enfasis = cargar['enfasis']
                evaluaciones.nombre_jurado1 = cargar['nombre_jurado1']
                evaluaciones.nombre_jurado2 = cargar['nombre_jurado2']
                evaluaciones.inicilizar = cargar['inicilizar']
                evaluaciones.nota = cargar['nota']
                evaluaciones.comentario_final = cargar['comentario_final']
                evaluaciones.correciones = cargar['correciones']
                evaluaciones.recomendacion = cargar['recomendacion']
                arreglo.append(evaluaciones)
            self.evaluaciones = arreglo

    def listar_nombres(self):
        lista_nombres = []
        for evaluaciones in self.evaluaciones:
            lista_nombres.append(evaluaciones.nombre_autor)
            if len(evaluaciones.calificacion) > 0:  # este if sirve para saber si si ya se califico un estudiante y no calificarlo dos veces
                lista_nombres.pop()
        return lista_nombres

    def listar_nombres_calificados(self):
        lista_nombres = []
        for nombres in self.evaluaciones:
            if len(nombres.calificacion) > 0:
                lista_nombres.append(
                    nombres.nombre_autor)  # el ciclo recorre el arreglo que tiene todas las calificaciones y guarda en el arreglo los nombres calificados
        return lista_nombres

    def mejor_calificacion(self):
        mejor_calificacion = EvaluacionEstudiante()
        # recorre todos los estudiantes calificados para buscar el que tenga mayor nota final
        for i in self.evaluaciones:
            if i.nota > mejor_calificacion.nota:
                mejor_calificacion = i
        return mejor_calificacion

    def listar_notas(self):
        notas = []
        for i in self.evaluaciones:
            # revisa que los nombres que se van a agregar a la grafica ya esten calificados y no solo inicilizados
            if len(i.calificacion) > 0:
                notas.append(i.nota)
        return notas

    def contar_calificados(self):
        cantidad = 0
        # cuenta el numero de estudiates calificados
        for personas in self.evaluaciones:
            if len(personas.calificacion) > 0:
                cantidad += 1
        return cantidad

    def promedio_notas_criterios(self, notas, cantidad, criterios_controller):
        # recorre cada una de las calificaciones y realiza la sumatoria de la nota de cada criterio por estudiante
        for i in self.evaluaciones:
            for j in range(len(notas)):
                if len( i.calificacion ) > 0 and len( notas ) <= len(i.calificacion) and i.calificacion[j].identificador == criterios_controller.criterios[j].identificador: # revisa que solo se tenga en cuenta a personas que ya se calificaron
                    notas[j] += i.calificacion[j].nota_final
        # saca el promedio de las notas
        for k in range(len(notas)):
            if cantidad > 0:
                notas[k] /= cantidad