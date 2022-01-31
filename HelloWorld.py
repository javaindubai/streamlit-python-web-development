import streamlit as st

st.set_page_config(
    page_title='Introduction, Installation and HelloWorld',
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                .css-1l40rdr { text-align: left;}
                .css-sc0g0 { text-align: center;}
                #h1 { color: #431c5d }
                #h1 { color: #bccbde }
                #h1 { color: #cdd422 }
                #h1 { color: #3fb0ac }
                h1 { color: #431c5d }
                h2 { color: #431c5d }
                h3 { color: #3fb0ac }
                .css-145kmo2 { color: #3fb0ac }
                .css-h9oeas { color: #431c5d }
                .css-hi6a2p { max-width: 60% }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Welcome to Streamlit Web Development Session")


def main():
    style_sidebar()
    main_body()
    return None


def style_sidebar():
    st.sidebar.markdown('''
    <small>This session Tutor [Javalingappa](https://www.linkedin.com/in/javalingappa/), Download code here  [Github](https://github.com/javaindubai/streamlit-python-web-development/tree/s1_install_hellowworld).</small>
        ''', unsafe_allow_html=True)
    st.sidebar.header('Introduction, Installation and HelloWorld')
    st.sidebar.markdown('__How to install and import__')
    st.sidebar.code('pip install streamlit')
    st.sidebar.markdown('__How to run default streamlit hello__')
    st.sidebar.code('streamlit hello')
    st.sidebar.markdown('__Import convention__')
    st.sidebar.code('>>> import streamlit as st')
    st.sidebar.markdown('__How to run Streamlit app__')
    st.sidebar.code('streamlit run MainScriptName.py')
    st.sidebar.markdown('__How to check Streamlit Version__')
    st.sidebar.code('streamlit --version')
    st.sidebar.markdown('__How to check python Version__')
    st.sidebar.code('python -V')
    st.sidebar.markdown('__How to check Anaconda Version__')
    st.sidebar.code('conda -V')
    st.sidebar.markdown('__How to run default streamlit hello__')
    st.sidebar.code('streamlit hello')


def main_body():
    exp1 = st.expander("How to create Python Virtual Environment in Command Prompt", expanded=False)
    with exp1:
        # st.subheader("How to create Python Virtual Environment in Command Prompt")
        st.write('**any_path_to_virtual_env** = C:/Streamlit/PythonVirtualEnv')
        st.markdown('__Create Python Virtual Env__')
        st.code('python -m venv C:/Streamlit/PythonVirtualEnv')
        st.markdown('__Activate Python Virtual Env__')
        st.code('''
            cd C:/Streamlit/PythonVirtualEnv
    C:/Streamlit/PythonVirtualEnv>Script/activate.bat
              ''')
        st.markdown('__Install Streamlit__')
        st.code('pip install streamlit')
        st.markdown('__Deactivate Python Virtual Env__')
        st.code('''
                  cd C:/Streamlit/PythonVirtualEnv
          C:/Streamlit/PythonVirtualEnv>Script/deactivate.bat
                    ''')

    exp2 = st.expander("How to create Conda  Environment in Command Promp", expanded=False)
    with exp2:
        st.markdown('__Create Conda Env__')
        st.code('conda create -n DemoEnv python=3.9')
        st.markdown('__Activate Conda Environment__')
        st.code('conda activate DemoEnv')
        st.markdown('__Install Streamlit__')
        st.code('pip install streamlit')
        st.markdown('__Deactivate Conda Environment__')
        st.code('conda deactivate')
    exp3 = st.expander("How to create Conda  Environment in PyCharm IDE", expanded=False)
    with exp3:
        st.image('conda_pycharm.PNG')


if __name__ == '__main__':
    main()
