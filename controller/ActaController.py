import json
from model.Acta import PDF

class ActaController:
    def __init__(self) -> None:
        super().__init__()
        self.actas = []

    def agregar_acta(self, acta_obj):
        self.actas.append(acta_obj)

    # esta funcion sirve para cargar en un .json las actas y guardarlas para que no se borren cada vez que se ejecuta el programa

    def cargar(self):
        lista = []
        # convierte las actas en diccionarios para poder guardalas dentro de un .json
        for i in self.actas:
            diccionario = {'fuente': '', 'inicializar': '', 'nombre_pdf': '', 'fecha': '', 'num_acta': '', 'titulo': '',
                           'autor': '', 'id': '', 'periodo': '', 'director': '', 'codirector': '', 'enfasis': '',
                           'modalidad': '', 'jurado1': '', 'jurado2': '', 'num_criterio': '', 'nombre_criterio': '',
                           'ponderacion': '', 'calificacion': '', 'observacion': '', 'calificacion_final': '',
                           'unidad': '', 'decima': '', 'comentario_final': '', 'correcciones': '', 'recomendacion': ''}
            diccionario['fuente'] = i.fuente
            diccionario['inicializar'] = i.inicializar
            diccionario['nombre_pdf'] = i.nombre_pdf
            diccionario['fecha'] = i.fecha
            diccionario['num_acta'] = i.num_acta
            diccionario['titulo'] = i.titulo
            diccionario['autor'] = i.autor
            diccionario['id'] = i.id
            diccionario['periodo'] = i.periodo
            diccionario['director'] = i.director
            diccionario['codirector'] = i.codirector
            diccionario['enfasis'] = i.enfasis
            diccionario['modalidad'] = i.modalidad
            diccionario['jurado1'] = i.jurado1
            diccionario['jurado2'] = i.jurado2
            diccionario['num_criterio'] = i.num_criterio
            diccionario['nombre_criterio'] = i.nombre_criterio
            diccionario['ponderacion'] = i.ponderacion
            diccionario['calificacion'] = i.calificacion
            diccionario['observacion'] = i.observacion
            diccionario['calificacion_final'] = i.calificacion_final
            diccionario['unidad'] = i.unidad
            diccionario['decima'] = i.decima
            diccionario['comentario_final'] = i.comentario_final
            diccionario['correcciones'] = i.correcciones
            diccionario['recomendacion'] = i.recomendacion
            lista.append(diccionario)
        # carga la informacion dentro del .json
        with open('data_actas.json', 'w') as outfile:
            json.dump(lista, outfile)

    def leer(self):
        with open('data_actas.json') as json_file:
            data = json.load(json_file)
            lista = []
            for crear in data:
                cargar_acta = PDF('P', 'mm', 'Letter')
                cargar_acta.fuente = crear['fuente']
                cargar_acta.inicializar = crear['inicializar']
                cargar_acta.nombre_pdf = crear['nombre_pdf']
                cargar_acta.fecha = crear['fecha']
                cargar_acta.num_acta = crear['num_acta']
                cargar_acta.titulo = crear['titulo']
                cargar_acta.autor = crear['autor']
                cargar_acta.id = crear['id']
                cargar_acta.periodo = crear['periodo']
                cargar_acta.director = crear['director']
                cargar_acta.codirector = crear['codirector']
                cargar_acta.enfasis = crear['enfasis']
                cargar_acta.modalidad = crear['modalidad']
                cargar_acta.jurado1 = crear['jurado1']
                cargar_acta.jurado2 = crear['jurado2']
                cargar_acta.num_criterio = crear['num_criterio']
                cargar_acta.nombre_criterio = crear['nombre_criterio']
                cargar_acta.ponderacion = crear['ponderacion']
                cargar_acta.calificacion = crear['calificacion']
                cargar_acta.observacion = crear['observacion']
                cargar_acta.calificacion_final = crear['calificacion_final']
                cargar_acta.unidad = crear['unidad']
                cargar_acta.decima = crear['decima']
                cargar_acta.comentario_final = crear['comentario_final']
                cargar_acta.correcciones = crear['correcciones']
                cargar_acta.recomendacion = crear['recomendacion']
                lista.append(cargar_acta)
        self.actas = lista

    #Da una lista con todos los nombres de los pdfs
    def listar_nombre(self):
        actas_nombres = []
        for acta in self.actas:
            actas_nombres.append(acta.nombre_pdf)
        return actas_nombres
