import streamlit as st


def main(topic):
    st.header(str(topic))
    sub = None
    sub = 'Text Elements and Sidebar'
    style_sidebar(sub, topic)
    main_body(sub)
    return None


def style_sidebar(sub, topic):
    if sub is None or sub == '':
        sub = str(topic)
    st.sidebar.subheader(str(sub))
    st.sidebar.video('https://www.youtube.com/watch?v=NgR5u6w4MRg&t=5s')


def main_body(sub):
    st.subheader(str(sub))
    exp0 = st.expander("Watch Full Video Of "+str(sub)+" Tutorial")
    with exp0:
        st.video('https://www.youtube.com/watch?v=idhnmL5x4Q8')

    exp1 = st.expander("Text Elements and Sidebar Output")
    with exp1:
        welcome = "Welcome to Text Elements"

        st.title("st.title  => " + welcome)
        st.header("st.title  => " + welcome)
        st.subheader("st.title  => " + welcome)
        st.text("st.title  => " + welcome)
        st.write("st.title  => " + welcome)
        st.markdown("st.title  => " + welcome)
        st.code("st.title  => " + welcome)
        st.caption("st.title  => " + welcome)
        st.latex("st.title  => " + welcome)
        welcome

        st.write("""st.write()""")
        st.write(""" **st.write(body, anchor=None)** :: *Display text in title formatting.* """)
        st.markdown("----")

        st.title("""st.title()""")
        st.title(""" **st.title(body, anchor=None)** :: *Display text in title formatting.* """)
        st.markdown("----")

        textElements = ['title', 'header', 'subheader', 'text', 'caption', 'markdown', 'code', 'latex', 'write', 'magic']
        item = st.selectbox('Select Any Text Element', textElements)

        if item == 'title':
            st.write(""" **st.title(body, anchor=None)** :: *Display text in title formatting.*
        
                    Documentation: 
        
                    Each document should have a single `st.title()`, although this is not
                    enforced.
        
                    Parameters
                    ----------
                        body : str
                            The text to display.
        
                        anchor : str
                            The anchor name of the header that can be accessed with #anchor
                            in the URL. If omitted, it generates an anchor using the body.
        
        
                    Example
                    -------
                        >>> st.title('This is a title')
        
                    OUTPUT:
                    -------
                    """)
            st.title('This is a title')

        if item == 'header':
            st.write(""" **st.header(body, anchor=None)** :: *Display text in header formatting.*
                Documentation: 
        
                Parameters
                ----------
                body : str
                    The text to display.
        
                anchor : str
                    The anchor name of the header that can be accessed with #anchor
                    in the URL. If omitted, it generates an anchor using the body.
        
                Example
                -------
                >>> st.header('This is a header')
        
                OUTPUT:
                -------
                """)
            st.header('This is a header')

        if item == 'subheader':
            st.write(""" **st.subheader(body, anchor=None)** :: *Display text in subheader formatting.*
                Documentation: 
        
                Parameters
                ----------
                body : str
                    The text to display.
        
                anchor : str
                    The anchor name of the header that can be accessed with #anchor
                    in the URL. If omitted, it generates an anchor using the body.
        
                Example
                -------
                >>> st.subheader('This is a subheader')
        
                OUTPUT:
                -------
                """)
            st.subheader('This is a subheader')

        if item == 'text':
            st.write(""" **st.text(body)** :: *Write fixed-width and preformatted text.*
                Documentation: 
        
                Parameters
                ----------
                body : str
                    The string to display.
        
                Example
                -------
                >>> st.text('This is some text.')
        
                OUTPUT:
                -------
                """)
            st.text('This is some text.')

        name = 'Java'

        st.write('Below is a DataFrame:', name, 'Above is a dataframe.')

        x = 10
        'x', x

        st.sidebar.markdown('''
        # Sections
        - [Title Section](#title)
            * [Subheader First Section](#first)
        - [Header Section](#header)
            * [Subheader Second Section](#second)
        ''', unsafe_allow_html=True)

        st.title('Welcome to Title Section', anchor='title-demo-anchor')
        for i in range(0, 20):
            st.write('Hello - ' + str(i))

        st.subheader('Welcome to SubHeader Section first', anchor='subheader-first')
        for i in range(0, 5):
            st.write('I am Java - ' + str(i))

        st.markdown("[Jump to Title Section](#title-demo-anchor)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader First Section](#subheader-first)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader Second Section](#subheader-second)", unsafe_allow_html=True)

        st.header('Welcome to Header Section', anchor='header-demo-anchor')
        for i in range(0, 20):
            st.write('How are you - ' + str(i))

        st.subheader('Welcome to SubHeader Section second', anchor='subheader-second')
        for i in range(0, 4):
            st.write('I am Fine - ' + str(i))

        st.markdown("[Jump to Title Section](#title-demo-anchor)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader First Section](#subheader-first)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader Second Section](#subheader-second)", unsafe_allow_html=True)
        st.markdown("[Jump to Header Section](#header-demo-anchor)", unsafe_allow_html=True)

        st.latex(r'''
             (a + b)^2 = a^2 + b^2 + 2ab
             ''')

        st.latex(r'''
             a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
             \sum_{k=0}^{n-1} ar^k =
             a \left(\frac{1-r^{n}}{1-r}\right)
             ''')

    with st.expander("Check Code Here"):
        st.code("""
        welcome = "Welcome to Text Elements"
        # title, header, subheader, text, write, markdown, code, caption, latex and sidebar
        st.title("st.title  => " + welcome)
        st.header("st.title  => " + welcome)
        st.subheader("st.title  => " + welcome)
        st.text("st.title  => " + welcome)
        st.write("st.title  => " + welcome)
        st.markdown("st.title  => " + welcome)
        st.code("st.title  => " + welcome)
        st.caption("st.title  => " + welcome)
        st.latex("st.title  => " + welcome)
        welcome
        
        st.write('''st.write()''')
        st.write(''' **st.write(body, anchor=None)** :: *Display text in title formatting.* ''')
        st.markdown("----")
        
        st.title('''st.title()''')
        st.title(''' **st.title(body, anchor=None)** :: *Display text in title formatting.* ''')
        st.markdown("----")
        
        textElements = ['title', 'header', 'subheader', 'text', 'caption', 'markdown', 'code', 'latex', 'write', 'magic']
        item = st.selectbox('Select Any Text Element', textElements)
        
        if item == 'title':
            st.write(''' **st.title(body, anchor=None)** :: *Display text in title formatting.*
        
                    Documentation: 
        
                    Each document should have a single `st.title()`, although this is not
                    enforced.
        
                    Parameters
                    ----------
                        body : str
                            The text to display.
        
                        anchor : str
                            The anchor name of the header that can be accessed with #anchor
                            in the URL. If omitted, it generates an anchor using the body.
        
        
                    Example
                    -------
                        >>> st.title('This is a title')
        
                    OUTPUT:
                    -------
                    ''')
            st.title('This is a title')
        
        if item == 'header':
            st.write(''' **st.header(body, anchor=None)** :: *Display text in header formatting.*
                Documentation: 
        
                Parameters
                ----------
                body : str
                    The text to display.
        
                anchor : str
                    The anchor name of the header that can be accessed with #anchor
                    in the URL. If omitted, it generates an anchor using the body.
        
                Example
                -------
                >>> st.header('This is a header')
        
                OUTPUT:
                -------
                ''')
            st.header('This is a header')
        
        if item == 'subheader':
            st.write(''' **st.subheader(body, anchor=None)** :: *Display text in subheader formatting.*
                Documentation: 
        
                Parameters
                ----------
                body : str
                    The text to display.
        
                anchor : str
                    The anchor name of the header that can be accessed with #anchor
                    in the URL. If omitted, it generates an anchor using the body.
        
                Example
                -------
                >>> st.subheader('This is a subheader')
        
                OUTPUT:
                -------
                ''')
            st.subheader('This is a subheader')
        
        if item == 'text':
            st.write(''' **st.text(body)** :: *Write fixed-width and preformatted text.*
                Documentation: 
        
                Parameters
                ----------
                body : str
                    The string to display.
        
                Example
                -------
                >>> st.text('This is some text.')
        
                OUTPUT:
                -------
                ''')
            st.text('This is some text.')
        
        name = 'Java'
        
        st.write('Below is a DataFrame:', name, 'Above is a dataframe.')
        
        x = 10
        'x', x
        
        st.sidebar.markdown('''
        # Sections
        - [Title Section](#title)
            * [Subheader First Section](#first)
        - [Header Section](#header)
            * [Subheader Second Section](#second)
        ''', unsafe_allow_html=True)
        
        st.title('Welcome to Title Section', anchor='title-demo-anchor')
        for i in range(0, 20):
            st.write('Hello - ' + str(i))
        
        st.subheader('Welcome to SubHeader Section first', anchor='subheader-first')
        for i in range(0, 5):
            st.write('I am Java - ' + str(i))
        
        st.markdown("[Jump to Title Section](#title-demo-anchor)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader First Section](#subheader-first)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader Second Section](#subheader-second)", unsafe_allow_html=True)
        
        st.header('Welcome to Header Section', anchor='header-demo-anchor')
        for i in range(0, 20):
            st.write('How are you - ' + str(i))
        
        st.subheader('Welcome to SubHeader Section second', anchor='subheader-second')
        for i in range(0, 4):
            st.write('I am Fine - ' + str(i))
        
        st.markdown("[Jump to Title Section](#title-demo-anchor)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader First Section](#subheader-first)", unsafe_allow_html=True)
        st.markdown("[Jump to Subheader Second Section](#subheader-second)", unsafe_allow_html=True)
        st.markdown("[Jump to Header Section](#header-demo-anchor)", unsafe_allow_html=True)
        
        st.latex(r'''
             (a + b)^2 = a^2 + b^2 + 2ab
             ''')
        
        st.latex(r'''
             a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
             \sum_{k=0}^{n-1} ar^k =
             a \left(\frac{1-r^{n}}{1-r}\right)
             ''')
    """, language='python')
