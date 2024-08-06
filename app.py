import streamlit as st

st.title("Soy una aplicación de Streamlit: Sumando 3 valores")

st.write("Hola voy a sumar 3 valores")

numero1 = st.number_input("Introduce tu primer numero:", min_value=1.0)
numero2 = st.number_input("Introduce tu segundo numero:", min_value=1.0)
numero3 = st.number_input("Introduce tu tercer numero:", min_value=1.0)

suma = numero1 + numero2 + numero3

st.write(f"La suma de {numero1} + {numero2} es: {suma}")