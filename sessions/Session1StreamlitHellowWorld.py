import streamlit as st


def main(topic):
    st.header(str(topic))
    sub = 'Introduction, Installation and HelloWorld'
    style_sidebar(sub, topic)
    main_body(sub)
    return None


def style_sidebar(sub, topic):
    st.sidebar.subheader(sub)
    st.sidebar.video('https://www.youtube.com/watch?v=FV1AXGzSZLk')
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


def main_body(sub):
    exp0 = st.expander("Watch Full Video Of "+str(sub)+" Tutorial")
    with exp0:
        st.video('https://www.youtube.com/watch?v=alRsmcb_uLQ')
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
    exp4 = st.expander("Softwares Download Links", expanded=False)
    with exp4:
        st.markdown(''' <medium>Download [Python](https://www.python.org/downloads/)</medium> ''', unsafe_allow_html=True)
        st.markdown(''' <medium>Download [Anaconda](https://www.anaconda.com/products/individual/)</medium> ''', unsafe_allow_html=True)
        st.markdown(''' <medium>Download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)</medium> ''', unsafe_allow_html=True)
        st.markdown(''' <medium>Download [Code](https://github.com/javaindubai/streamlit-python-web-development/tree/s1_install_hellowworld)</medium> ''', unsafe_allow_html=True)

# if __name__ == '__main__':
#     main()
