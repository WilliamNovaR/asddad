class Acciones:
    def __init__(self) -> None:
        super().__init__()
        self.acciones = ["Home", 'Crear cuenta', 'Iniciar sesion']
        self.iconos = [ 'house', 'person-plus', 'person-check' ]

    def agregar_evaluacion(self, evaluacion_obj):
        self.evaluaciones.append(evaluacion_obj)

    #esta metodo sirve para establecer las funciones y acciones que cada tipo de usario tendra disponible en el menu
    def menu_acciones(self, tipo):
        if tipo == 'Asistente':
            self.acciones = ['Home', 'Crear cuenta', 'Iniciar sesion',
                                           # este arreglo tiene las opciones de menu que se tendra si se inicia de cuenta asistente
                                           'Inicilizar datos actas', 'Ver historico resumido actas',
                                           'Estadisticas', 'Cerrar sesion']
            self.iconos = ['house', 'person-plus', 'person-check', 'upload', 'book',
                                         # en este arreglo se cargan los iconos que tendran cada uno de las opciones de menu
                                         'file-bar-graph', 'person-x']
        elif tipo == 'Jurado':
            self.acciones = ['Home', 'Crear cuenta', 'Iniciar sesion', 'Evaluar nuevo trabajo',
                                           'Ver o editar calificaciones', 'Exportar acta', 'Estadisticas',
                                           'Cerrar sesion']
            self.iconos = ['house', 'person-plus', 'person-check', 'clipboard',
                                         'clipboard-check', 'file-pdf', 'file-bar-graph', 'person-x']
        elif tipo == 'Director/a':
            self.acciones = ['Home', 'Crear cuenta', 'Iniciar sesion',
                                           'Modificar y ver criterios',
                                           'Ver historico resumido actas', 'Estadisticas', 'Cerrar sesion']
            self.iconos = ['house', 'person-plus', 'person-check', 'list-check',
                                         'book', 'file-bar-graph', 'person-x']