import streamlit as st


def main():
    st.text("Please click Previous or Next Topic get more information")
    style_sidebar()

    return None


def style_sidebar():
    st.sidebar.title("Hi !! Streamlit-Python-Web")
    st.sidebar.markdown('''
    <small>This session Tutor [Javalingappa](https://www.linkedin.com/in/javalingappa/), Download code here  [Github](https://github.com/javaindubai/streamlit-python-web-development/tree/s1_install_hellowworld).</small>
        ''', unsafe_allow_html=True)

