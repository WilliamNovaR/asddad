from model.Criterio import Criterio
import json
from model.Criterio import Criterio


class CriterioController:
    def __init__(self) -> None:
        super().__init__()
        self.criterios = []
        criterio = Criterio("Desarrollo y profundidad en el tratamiento del tema", "", 0.20 )
        self.criterios.append( criterio )
        criterio = Criterio("Desafio academico y cientifico del tema", "", 0.15)
        self.criterios.append(criterio)
        criterio = Criterio("Cumplimiento de los objetivos propuestos", "", 0.10)
        self.criterios.append(criterio)
        criterio = Criterio("Creatividad e innovacion de las soluciones y desarrollos propuestos", "" , 0.10)
        self.criterios.append(criterio)
        criterio = Criterio("Validez de los resultados y concluciones", "", 0.20)
        self.criterios.append(criterio)
        criterio = Criterio("Manejo y procedimiento de la informacion y bibliografia", "", 0.10)
        self.criterios.append(criterio)
        criterio = Criterio("Calidad y presentacion del documento escrito ", "", 0.075)
        self.criterios.append(criterio)
        criterio = Criterio("Presentacion oral", "", 0.075)
        self.criterios.append(criterio)

    def agregar_criterios(self, criterios_obj):
        self.criterios.append(( criterios_obj ))

    def ponderacion_final(self):
        suma = 0
        for criterio in self.criterios:
            if suma + criterio.porcentaje_ponderacion <= 1:
                suma += criterio.porcentaje_ponderacion
            else:
                raise ValueError( "la sumatoria de los porcentajes de ponderacion de los criterios superan el 100%" )
        return suma

    # esta funcion sirve para cargar en un .json los criterios y guardarlas para que no se borren cada vez que se ejecuta el programa
    def cargar(self):
        lista = []
        # convierte en un diccionario los criterios para poderlos cargar en el .json
        for i in self.criterios:
            diccionario = {'identificador': '', 'descripcion': '', 'porcentaje_ponderacion': ''}
            diccionario['identificador'] = i.identificador
            diccionario['descripcion'] = i.descripcion
            diccionario['porcentaje_ponderacion'] = i.porcentaje_ponderacion
            lista.append(diccionario)
        # carga la informacion dentro del .json
        with open('data_criterios.json', 'w') as outfile:
            json.dump(lista, outfile)

    def leer(self):
        with open('data_criterios.json') as json_file:
            data = json.load(json_file)
            lista = []
            for crear in data:
                cargar_cuenta = Criterio(crear['identificador'], crear['descripcion'], crear['porcentaje_ponderacion'])
                lista.append(cargar_cuenta)
        self.criterios = lista

    #retorna una lista con los nombres de los criterios
    def listar_nombre(self):
        criterios = []
        for criterio in self.criterios:
            criterios.append(criterio.identificador)
        return criterios

    def lista_numero_criterios(self):
        numeros_criterio = []
        for i in range(len(self.criterios)):
            numeros_criterio.append(i + 1)  # establece un numero para cada criterio
        return numeros_criterio

    def arreglo_criterios(self):
        notas = []
        for name in self.criterios:
            notas.append(0)  # crea los espacios en el arreglo para guardar el promedio de notas
        return notas



