import time

import streamlit as st


def main(topic):
    st.header("Session-2 : "+str(topic))
    style_sidebar()
    main_body()
    return None


def style_sidebar():
    st.sidebar.title("Streamlit-Python-Web")
    st.sidebar.markdown('''
    <small>This session Tutor [Javalingappa](https://www.linkedin.com/in/javalingappa/), Download code here  [Github](https://github.com/javaindubai/streamlit-python-web-development/tree/s1_install_hellowworld).</small>
        ''', unsafe_allow_html=True)


def main_body():
    exp0 = st.expander("Watch Video Here-Coming soon..")
    with exp0:
        st.subheader("Coming Soon...")

