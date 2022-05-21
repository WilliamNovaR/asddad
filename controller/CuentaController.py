import json
from model.Cuenta import Cuenta

class Cuentas:
    def __init__(self) -> None:
        super().__init__()
        self.cuentas = []

    def agregar_cuenta(self, acta_obj):
        self.cuentas.append(acta_obj)

    # esta funcion sirve para guardar las cuentas dentro de un .json
    def cargar(self):
        lista = []
        # se recorren todos los elementos dentro de cuentaController para guardarlo en un diccionario para poder guardarlo en el .json
        for i in self.cuentas:
            diccionario = {'usuario': '', 'contrasena': '', 'tipo': ''}
            diccionario['usuario'] = i.usuario
            diccionario['contrasena'] = i.contrasena
            diccionario['tipo'] = i.tipo
            lista.append(diccionario)
        # se abre y se guarda el diccionario en el .json
        with open('data_cuentas.json', 'w') as outfile:
            json.dump(lista, outfile)

    def leer(self):
        with open('data_cuentas.json') as json_file:
            data = json.load(json_file)
            lista = []
            for crear in data:
                cargar_cuenta = Cuenta()
                cargar_cuenta.usuario = crear['usuario']
                cargar_cuenta.contrasena = crear['contrasena']
                cargar_cuenta.tipo = crear['tipo']
                lista.append(cargar_cuenta)
        self.cuentas = lista