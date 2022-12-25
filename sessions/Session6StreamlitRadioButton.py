import streamlit as st
from streamlit import session_state

import core.StreamlitRadioFeatures as radio

if 'chkPageSelected' not in session_state.keys():
    session_state['chkPageSelected'] = ''

def onchange_radio():
    session_state['chkPageSelected'] = session_state['pageSelected']

def main(topic):
    st.header(str(topic))
    sub = 'Streamlit Radio Button Basics & Advance Features'
    style_sidebar(sub, topic)
    main_body(sub)
    return None


def style_sidebar(sub, topic):
    if sub is None or sub == '':
        sub = str(topic)
    st.sidebar.subheader(sub)
    st.sidebar.video('https://www.youtube.com/watch?v=idhnmL5x4Q8')
    pages = {
        'Radio Basic Examples': radio,
        'Radio Advance Examples': radio,
    }
    st.sidebar.radio("Select Feature", tuple(pages.keys()), key='pageSelected', on_change=onchange_radio)


def main_body(sub):
    st.subheader(sub)
    exp0 = st.expander("Watch Full Video Of " + str(sub))
    with exp0:
        st.video('https://www.youtube.com/watch?v=alRsmcb_uLQ')

    exp1 = st.expander(str(sub) + " Output")
    with exp1:
        if session_state['chkPageSelected'] == 'Radio Basic Examples':
            radio.radio_basic_examples()
        elif session_state['chkPageSelected'] == 'Radio Advance Examples':
            radio.radio_advance_examples()
        else:
            radio.radio_basic_examples()
    exp2 = st.expander(str(sub) + " Code")
    with exp2:
        st.code("""
        
        """, language='python')