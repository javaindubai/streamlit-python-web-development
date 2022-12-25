import streamlit as st


def main(topic):
    st.header(str(topic))
    sub = 'Streamlit Title Element'
    style_sidebar(sub, topic)
    main_body(sub)
    return None


def style_sidebar(sub, topic):
    if sub is None or sub == '':
        sub = str(topic)
    st.sidebar.subheader(sub)
    st.sidebar.video('https://www.youtube.com/watch?v=hLGUvZAtQNE')


def main_body(sub):
    st.subheader(sub)
    exp0 = st.expander("Watch Full Video Of "+str(sub)+" Tutorial")
    with exp0:
        st.video('https://www.youtube.com/watch?v=hLGUvZAtQNE')

    exp1 = st.expander(str(sub)+" Output")
    with exp1:
        st.title('st.title demo', 'sttitle')
        for i in range(1, 5):
            st.write('Display text in title formatting')
        st.title(body='i am message body', anchor='I_am_anchor')
        for j in range(1, 5):
            st.write('st.title(body, anchor) ')
        st.markdown('----')

        st.markdown('<h1> I am html h1 tag</h1>', unsafe_allow_html=True)
        for k in range(1, 5):
            st.write('st.title demo')
        st.title("st.title is equivalent to html h1 tag")
        for l in range(1, 5):
            st.write('hope you understood st.title')

        st.markdown('[Top](#sttitle)', unsafe_allow_html=True)
        st.markdown('[Jump to I_am_anchor](#I_am_anchor)', unsafe_allow_html=True)
        st.markdown('----')
        st.title('Thank You')

        st.title('Share and Advice')

    exp2 = st.expander(str(sub) + " Output")
    with exp2:
        st.code("""
          st.title('st.title demo', 'sttitle')
        for i in range(1, 5):
            st.write('Display text in title formatting')
        st.title(body='i am message body', anchor='I_am_anchor')
        for j in range(1, 5):
            st.write('st.title(body, anchor) ')
        st.markdown('----')

        st.markdown('<h1> I am html h1 tag</h1>', unsafe_allow_html=True)
        for k in range(1, 5):
            st.write('st.title demo')
        st.title("st.title is equivalent to html h1 tag")
        for l in range(1, 5):
            st.write('hope you understood st.title')

        st.markdown('[Top](#sttitle)', unsafe_allow_html=True)
        st.markdown('[Jump to I_am_anchor](#I_am_anchor)', unsafe_allow_html=True)
        st.markdown('----')
        st.title('Thank You')

        st.title('Share and Advice')      

        """, language='python')