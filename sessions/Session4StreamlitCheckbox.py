import streamlit as st
from streamlit import session_state

import core.StreamlitCheckboxFeatures as checkbox

if 'chkPageSelected' not in session_state.keys():
    session_state['chkPageSelected'] = ''

def onchange_checkbox():
    session_state['chkPageSelected'] = session_state['pageSelected']

def main(topic):
    st.header(str(topic))
    sub = 'Streamlit Checkbox Basics and Advance Features'
    style_sidebar(sub, topic)
    main_body(sub)
    return None


def style_sidebar(sub, topic):
    if sub is None or sub == '':
        sub = str(topic)
    st.sidebar.subheader(sub)
    st.sidebar.video('https://www.youtube.com/watch?v=idhnmL5x4Q8')
    pages = {
        'Checkbox Basic Examples': checkbox,
        'Checkbox Advance Examples': checkbox,
    }
    st.sidebar.radio("Select Feature", tuple(pages.keys()), key='pageSelected', on_change=onchange_checkbox)


def main_body(sub):
    st.subheader(sub)
    exp0 = st.expander("Watch Full Video Of " + str(sub))
    with exp0:
        st.video('https://www.youtube.com/watch?v=alRsmcb_uLQ')

    exp1 = st.expander(str(sub) + " Output")
    with exp1:
        if session_state['chkPageSelected'] == 'Checkbox Basic Examples':
            checkbox.checkbox_basic_examples()
        elif session_state['chkPageSelected'] == 'Checkbox Advance Examples':
            checkbox.checkbox_advance_examples()
        else:
            checkbox.checkbox_basic_examples()
    exp2 = st.expander(str(sub) + " Code")
    with exp2:
        st.code("""
        import streamlit as st
        
        def checkbox_basic_examples():
            st.subheader("Streamlit Checkbox basic Examples")
            st.checkbox('Unchecked')
            st.checkbox('Checked', value=True, key="DefaultChecked")
            st.checkbox('Default Disabled', value=False, key="dd", disabled=True)
            st.checkbox('Checked Disabled', value=True, key='cd', disabled=True)
            st.subheader('Read Checkbox status (checked/unchecked) Examples')
            isChecked = st.checkbox('One', key='one')
            st.write('Value of isChecked: ' + str(isChecked))
            if isChecked:
                st.write('CHECKED')
            else:
                st.write('UNCHECKED')
                st.subheader('Basic Examples Done')
        def checkbox_advance_examples():
            st.subheader("Streamlit Checkbox advance examples")
            st.checkbox('Send SMS', key='sms', help='Sending message to registered **mobile**', on_change=what_is_sending, args=('SMS',))
            st.checkbox('Send Email', key='email', on_change=what_is_sending, args=('Email',))
            st.checkbox('Send SMS and Email', key='emailsms', on_change=what_is_sending, args=('SMS and Email',))
            st.checkbox('Thank You', key='ty', value=True, disabled=True)
            st.checkbox('Share and Comment', key='sac', value=True, disabled=True)
            st.checkbox('Subscribe', key='s', value=True, disabled=True)
            st.markdown('----')
            st.subheader("End of Checkbox Tutorial")
            st.markdown('----')

        def what_is_sending(type: str):
            st.write("on_change is called and selected option : "+type)
        """, language='python')