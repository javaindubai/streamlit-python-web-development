import streamlit as st


def main(topic):
    st.header(str(topic))
    sub = None
    style_sidebar(sub, topic)
    main_body(sub)
    return None


def style_sidebar(sub, topic):
    if sub is None or sub == '':
        sub = str(topic)
    st.sidebar.subheader(sub)
    st.sidebar.video('https://www.youtube.com/watch?v=idhnmL5x4Q8')


def main_body(sub):
    st.subheader(sub)
    exp0 = st.expander("Watch Full Video Of "+str(sub))
    with exp0:
        st.video('https://www.youtube.com/watch?v=alRsmcb_uLQ')

    exp1 = st.expander(str(sub)+" Output")

    exp2 = st.expander(str(sub)+" Output")