# Importamos la librería Streamlit
import streamlit as st


def main():
    # Título y autor de la app
    st.title("Mi primera app")
    st.write("Esta app fue elaborada por Luisa Mazo")

    # Preguntamos el nombre al usuario
    nombre_usuario = st.text_input("Por favor, introduce tu nombre")

    # Verificamos si se ingresó un nombre
    if nombre_usuario:
        # Mostramos el mensaje de bienvenida
        st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")


if __name__ == "__main__":
    main()
