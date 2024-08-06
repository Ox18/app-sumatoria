import streamlit as st

st.title("Soy una aplicación de Streamlit")

st.write("Hola voy a sumar dos valores")

numero1 = st.number_input("Introduce tu primer numero:", min_value=1.0)
numero2 = st.number_input("Introduce tu segundo numero:", min_value=1.0)

suma = numero1 + numero2

st.write(f"La suma de {numero1} + {numero2} es: {suma}")