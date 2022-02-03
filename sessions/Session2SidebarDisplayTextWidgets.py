import time

import streamlit as st


def main(topic):
    st.header("Session-2 : " + str(topic))
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

    exp1 = st.expander("Example")
    with exp1:

        welcome = "Streamlit Text Elements"

        st.title("St.title() => " + welcome)
        st.header("St.header() => " + welcome)
        st.subheader("St.subheader() => " + welcome)
        st.latex("St.latex() => " + welcome)
        st.markdown("St.markdown() => " + welcome)
        st.write("St.write() => " + welcome)
        # magic text element - without any function it renders on the screen
        welcome
        st.text("St.text() => " + welcome)
        st.code("St.code() => " + welcome)
        st.caption("St.caption() => " + welcome)

        st.markdown("----")

        st.title("St.title() => <h1> tag ")
        st.header("St.header()=> <h2> tag ")
        st.subheader("St.subheader() => <h3> tag ")
        st.latex("St.latex() => font-size = 1.21em")
        st.markdown("St.markdown() => font-size = 1em = 16px")
        st.write("St.write() => => font-size = 1em = 16px")
        # magic text element => font-size = 1em = 16px" - without any function it renders on the screen
        welcome
        st.text("St.text() => font-size = 14px")
        st.code("St.code() => font-size = 14px")
        st.caption("St.caption() => font-size = 14px")

        # adding a <hr> tag

        st.markdown("----")

        st.subheader("st.code() example: ")

        st.code('''
        def add_two_numbers(a, b):
            return a +b
        st.write(add_two_numbers(25, 75))
        ''')
        st.caption("Result is: ")

        def add_two_numbers(a, b):
            return a + b

        st.write(add_two_numbers(25, 75))

        # adding a <hr> tag

        st.markdown("----")

        st.subheader("st.latex() Example: for (a+b)^2")

        st.latex(r'''
        (a+b)^2 = a^2 + b^2 + 2ab
        ''')

        st.latex(r'''
             a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
             \sum_{k=0}^{n-1} ar^k =
             a \left(\frac{1-r^{n}}{1-r}\right)
             ''')

        # adding a <hr> tag

        st.markdown("----")

        st.subheader("st.markdown and st.write special examples: ")

        st.markdown(':sunglasses:')
        st.write(':sunglasses:')
        st.write(':+1:')
        st.markdown(':+1:')
        st.write('**STREAMLIT**')
        st.write('*STREAMLIT*')
        st.markdown('- [x] Hello')
        st.write('- [x] Hello')

        # anchor and side bar examples

        st.title('Anchor and Sidebar Examples')
        st.markdown("----")

        st.title('Title Section', anchor='title')
        for i in range(0, 10):
            st.write("Hello - " + str(i))
        st.markdown("[Jump to Subheader Section First](#first)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader Section Second](#second)", unsafe_allow_html=True)
        st.title('Header Section', anchor='header')
        for i in range(0, 10):
            st.write("How are you - " + str(i))

        st.markdown("[Jump to Title Section](#title)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader Section First](#first)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader Section Second](#second)", unsafe_allow_html=True)

        st.title('Subheader Section First', anchor='first')
        for i in range(0, 10):
            st.write("I am Fine - " + str(i))

        st.markdown("[Jump to Title Section](#title)", unsafe_allow_html=True)
        st.markdown("[Jump to Header Section](#header)", unsafe_allow_html=True)

        st.title('Subheader Section Second', anchor='second')
        for i in range(0, 10):
            st.write("How about you - " + str(i))

        st.markdown("[Jump to Title Section](#title)", unsafe_allow_html=True)
        st.markdown("[Jump to Header Section](#header)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader Section First](#first)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader Section Second](#second)", unsafe_allow_html=True)

        # SIDEBAR

        st.sidebar.title("Welcome")

        st.sidebar.markdown('''
        # Sections
        - [Title Section](#title)
            * [Subheader First Section](#first)
        - [Header Section](#header)
            * [Subheader Second Section](#second)
        ''', unsafe_allow_html=True)
