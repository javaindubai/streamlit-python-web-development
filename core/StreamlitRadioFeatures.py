import streamlit as st
from streamlit import session_state


def radio_basic_examples():
    st.subheader("Streamlit radio basic Examples")
    st.radio('Options', options=['Unchecked', 'Checked'])
    st.radio('Options', options=['Unchecked', 'Checked'], index=1, key="DefaultChecked")
    st.radio('Options', options=['Unchecked', 'Checked'], disabled=True, key="r2")
    st.subheader('Read radio Selected Option Examples')
    opn = st.radio('Options', options=['One', 'Two', 'Three'], key='one')
    st.write('Selected Options: **' + str(opn)+'**')
    st.subheader('Basic Examples Done')


def radio_advance_examples():
    st.subheader("Streamlit Radio  advance examples")
    st.radio('Select Options', options=['Send SMS','Send Email','Send SMS and Email'], key='rOption', help='Sending message to registered **mobile**', on_change=what_is_selected)
    st.header('Thank You')
    st.subheader('Share and Comment')
    st.header('Subscribe')
    st.markdown('----')
    st.subheader("End of Streamlit Radio button Tutorial")
    st.markdown('----')


def what_is_selected():
    st.write("on_change is called and selected option : " + session_state['rOption'])
