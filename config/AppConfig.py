from sessions import Session1HellowWorld, Session2SidebarDisplayTextWidgets

config = dict()
config['topic_columns'] = ['Topic ID', 'Session', 'Title', 'Date']

search = dict()
search[''] = ''
search[
    'Installation Introduction and HelloWorld -                 Session-1 python install streamlit  pip install streamlit streamlit hello activate deactivate conda activate conda deactivate pyCharm IDE session1'] = 'Installation Introduction and HelloWorld'
search[
    'Streamlit Sidebar and Display Widgets -                    Session-2 Streamlit side bar st.sidebar() Text input st.text() display input st.header() header st.write() write Sub Header SubHeader st.subheader() caption st.caption() st.markdown() Mark Down HTML Latex st.latex() Code st.code() session2'] = 'Streamlit Sidebar and Display Widgets'

topics = dict()
topics['Installation Introduction and HelloWorld'] = [1, 'Session-1', 'Installation Introduction and HelloWorld', '31-01-2022', Session1HellowWorld]
topics['Streamlit Sidebar and Display Widgets'] = [2, 'Session-2', 'Streamlit Sidebar and Display Widgets', '04-02-2022', Session2SidebarDisplayTextWidgets]
