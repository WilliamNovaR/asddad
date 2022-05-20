import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from controller.memoria import Data
from controller.AccionesController import Acciones
from controller.CuentaController import Cuentas
from controller.EvalController import EvaluadorController
from controller.CriterioController import CriterioController
from controller.ActaController import ActaController
from view.Home import consultar_instrucciones
from view.sesion import crear_cuenta, iniciar_sesion, cerrar_sesion
from view.Evaluar import seleccion, agregar_evaluacion
from view.ConfigurarCriterios import seleccionar_opcion
from view.CrearActa import crearActa
from view.InicializarActa import agregar_datos
from view.InformacionActas import listar_actas
from view.AnaliticaDatos import escoger_analis
import os.path





class MainView:
    def __init__(self) -> None:
        super().__init__()

        # Estretagia para manejar el "estado" del controllador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            # Conexión con el controlador
            self.data = Data()
            self.acciones = Acciones()
            self.cuentas_controller = Cuentas()
            self.controller = EvaluadorController()
            self.criterios_controller = CriterioController()
            self.actas_controller = ActaController()

            st.session_state['main_view'] = self
        else:
            # Al exisir en la sesión entonces se actualizan los valores
            self.data = st.session_state.main_view.data
            self.acciones = st.session_state.main_view.acciones
            self.menu_actual = st.session_state.main_view.menu_actual
            self.cuentas_controller = st.session_state.main_view.cuentas_controller
            self.controller = st.session_state.main_view.controller
            self.criterios_controller = st.session_state.main_view.criterios_controller
            self.actas_controller = st.session_state.main_view.actas_controller
        self._dibujar_layout()
        #comprueba que los archivos esten creados para cargar los datos guardados en los .json y asi no se pierda la info
        if os.path.exists( 'data_cuentas.json' ):
            self.cuentas_controller.leer()
        if os.path.exists( 'data_criterios.json' ):
            self.criterios_controller.leer()
        if os.path.exists( 'data_actas.json' ):
            self.actas_controller.leer()
        if os.path.exists( 'data_calificaciones.json' ):
            self.controller.leer()




    def _dibujar_layout(self):
        img = Image.open("puj_logo_vertical_azul_copia.png") #carla la imagen del icono de la pagina
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Calificar trabajos finales", page_icon=img, layout="wide",
                            initial_sidebar_state="expanded")

        self.no_errores = 1
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3, self.col4, self.col5, self.col6, self.col7, self.col8 = st.columns(
            [1, 1, 1, 1, 1, 1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            self.menu_actual = option_menu("Menu",
                                        self.acciones.acciones,
                                        icons= self.acciones.iconos, menu_icon="cast")

    def controlar_menu(self):
        if self.menu_actual == "Home":
            consultar_instrucciones( st )
        elif self.menu_actual == 'Crear cuenta':
            crear_cuenta( st, self.cuentas_controller )
        elif self.menu_actual == 'Iniciar sesion':
            iniciar_sesion( st, self.cuentas_controller, self.acciones )
        elif self.menu_actual == "Inicilizar datos actas":
            agregar_datos(st, self.controller)
        elif self.menu_actual == "Modificar y ver criterios":
            seleccionar_opcion(st, self.criterios_controller)
        elif self.menu_actual == "Evaluar nuevo trabajo":
            agregar_evaluacion(st, self.controller, self.criterios_controller)
        elif self.menu_actual == "Ver o editar calificaciones":
            seleccion(st, self.controller, self.criterios_controller)
        elif self.menu_actual == "Exportar acta":
            crearActa(st, self.actas_controller, self.controller)
        elif self.menu_actual == "Ver historico resumido actas":
            listar_actas(st, self.criterios_controller, self.actas_controller)
        elif self.menu_actual == 'Estadisticas':
            escoger_analis(st, self.controller, self.criterios_controller)
        elif self.menu_actual == 'Cerrar sesion':
            cerrar_sesion(st, self.acciones)


# Main call

if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()
