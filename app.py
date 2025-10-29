import streamlit as st
st.title("Ejemplo para usar Session State")

if 'key' not in st.session_state:
  st.session_state['key'] = 'value'

count = 0 

increment = st.button ('Increment')
if increment:
  count += 1

st.write('Count _ ', count)
