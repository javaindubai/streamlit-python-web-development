import streamlit as st
from streamlit import session_state

import core.StreamlitRadioFeatures as radio

def main(topic):
    st.header(str(topic))
    sub = 'Streamlit App : Deployment on Heroku Cloud'
    style_sidebar(sub, topic)
    main_body(sub)
    return None


def style_sidebar(sub, topic):
    if sub is None or sub == '':
        sub = str(topic)
    st.sidebar.subheader(sub)
    st.sidebar.video('https://youtu.be/EqTVzPO0PcI')

def main_body(sub):
    st.subheader(sub)
    exp0 = st.expander("Watch Full Video Of " + str(sub))
    with exp0:
        st.video('https://youtu.be/EqTVzPO0PcI')

    exp1 = st.expander(str(sub) + " Output")
    with exp1:
        from PIL import Image
        img = Image.open('assets/python_techie_logo.PNG')
        # st.set_page_config(page_icon=img)
        st.title("Welcome to Heroku Deployment")
        st.markdown("----")
        st.subheader("How do we deploy Streamlit applications on Heroku?")
        st.image(img)
    exp2 = st.expander(str(sub) + " Code")
    with exp2:
        st.code("""
           from PIL import Image
        img = Image.open('logo.png')
        # st.set_page_config(page_icon=img)
        st.title("Welcome to Heroku Deployment")
        st.markdown("----")
        st.subheader("How do we deploy Streamlit applications on Heroku?")
        st.image(img)
        """, language='python')