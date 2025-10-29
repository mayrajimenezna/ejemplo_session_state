import streamlit as st
st.title("Ejemplo para usar Session State")

if 'count' not in st.session_state:
  st.session_state['key'] = 0


st.write('st.session_state)
