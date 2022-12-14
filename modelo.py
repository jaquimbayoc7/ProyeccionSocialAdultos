##Importar librerías de uso para el modelo
import numpy as np
import pickle
import streamlit as st

##Cargar el modelo
loaded_model = pickle.load(open('/home/julian/Documentos/ProyectoAdultoMayor/ProyeccionSocialAdultos/trained_model.sav','rb'))

##Logica del modelo predictivo
def puntuacion_prediction(input_data):

    input_data_as_array = np.asarray(input_data, dtype=float)

    input_reshaped = input_data_as_array.reshape(1,-1)

    prediccion = loaded_model.predict(input_reshaped)

    dato = abs(round(prediccion[0]/6,0))

    print(dato)

    if (dato >=0 and dato <=5):
        return 'Posibilidad de No Aprobación: {}'.format(dato)
    elif (dato >=6 and dato <=8):
        return 'Posibilidad Aprobación: {}'.format(dato)
    else:
        return 'Posibilidad de Ser el Mejor: {}'.format(dato)

##Activación del modelo con datos de la app
def main():

    st.markdown("<div><p style = 'text-align:center;'><img src='https://apps.corhuila.edu.co/AsistenciaCorhuila/src/LogoCorhuila.png' width='300px'></p></div>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: grey;'>Aplicación de Predicción de Puntuación Test Adulto Mayor</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: black;'>Programa de Ingeniería de Sistemas</h2>", unsafe_allow_html=True)
    
    ##Igual como estan en las variables de X en el dataframe
    st.subheader('Pregunta 1')
    st.text('La informática es:')
    st.text('1. Ciencia que estudia el uso de internet\n2. Ciencia que estudia el funcionamiento del computador\n3. Ciencia que estudia la gestión de información con medios electrónicos')
    P1 = st.text_input('Tu Respuesta es:')
    st.subheader('Pregunta 2')
    st.text('¿Qué es el software?:')
    st.text('1. Parte física de la computadora\n2. Parte tangible de la computadora\n3. Conjunto de programas de la computadora')
    P2 = st.text_input('Tu Respuesta es: ')
    st.subheader('Pregunta 3')
    st.text('Las partes de una computador son:')
    st.text('1. Monitor y CPU\n2. Pantalla, Torre o CPU, Teclado y Mouse\n3. Hardware y Software')
    P3 = st.text_input('Tu Respuesta es:  ')
    st.subheader('Pregunta 4')
    st.text('¿Qué es una carpeta?')
    st.text('1. Es un icono amarillo\n2. Es el contenedor de archivos, e incluso el contenedor de mismas carpetas\n3. Es un cuaderno donde se guarda informacion')
    P5 = st.text_input('Tu Respuesta es:   ')
    st.subheader('Pregunta 5')
    st.text('Indique su Edad')
    Edad = st.text_input('Tu Respuesta es:    ')
    st.subheader('Pregunta 6')
    st.text('Indique su Género\n 1. Masculino\n 2. Femenino')
    Genero = st.text_input('Tu Respuesta es:     ')
    
    prediccionF = ''
    
    if st.button('Resultado de la Predicción del Test'):
        prediccionF = puntuacion_prediction([P1, P2, P3, P5, Edad, Genero])
        
    st.success(prediccionF)
    
    
if __name__ == '__main__':
    main()


