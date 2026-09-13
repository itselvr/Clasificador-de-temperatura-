import streamlit as st

st.title("clasificador de temperatura")
temperatura = st. number_input("Introduce la temperatura en °C:", value=20)
if temperature< 10:
  st.write("hace frio.")
elif temperatura< 25:
  st.write("la temperatura es agradable.")
else:
  st.write("hace calor.")
