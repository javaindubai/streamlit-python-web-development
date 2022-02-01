import pandas as pd
import streamlit as st
from streamlit import session_state

from sessions import DefaultSession

st.set_page_config(
    page_title='Streamlit Python Web Development',
    layout="wide",
    initial_sidebar_state="expanded",
)

if 'topicIndexCount' not in session_state.keys():
    session_state['topicIndexCount'] = 0
if 'isNextButtonCLicked' not in session_state.keys():
    session_state['isNextButtonCLicked'] = False
if 'isPrevButtonCLicked' not in session_state.keys():
    session_state['isPrevButtonCLicked'] = False
if 'topicSelected' not in session_state.keys():
    session_state['topicSelected'] = ''

from config.AppConfig import topics, config, search

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                .css-1l40rdr { text-align: left;}
                .css-sc0g0 { text-align: center;}
                .css-18e3th9 { padding-top: 0px;}
                .css-zbg2rx { padding-top: 13%;}
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
# st.title("Welcome to Streamlit-Python-Web")

col1, col2, col3 = st.columns([1, 4, 1])
searchList = list(search.keys())

with col1:

    prev = st.button('Previous Topic')
    if prev:
        session_state['isPrevButtonCLicked'] = True
        if int(session_state['topicIndexCount']) <= 0:
            session_state['topicIndexCount'] = len(searchList) - 1
        else:
            session_state['topicIndexCount'] = session_state['topicIndexCount'] - 1
        session_state['topicSelected'] = search[searchList[session_state['topicIndexCount']]]
    else:
        session_state['isPrevButtonCLicked'] = False

with col2:
    st.write('')
    # if session_state['isPrevButtonCLicked'] or session_state['isNextButtonCLicked']:
    #     searchKey = st.selectbox('Search Your Interest', searchList, index=0)
    # else:
    #     searchKey = st.selectbox('Search Your Interest', searchList)
    # if searchKey != '' or (session_state['isPrevButtonCLicked'] == False and session_state['isNextButtonCLicked'] == False):
    #     session_state['topicIndexCount'] = searchList.index(searchKey)
    #     topic = search[searchList[session_state['topicIndexCount']]]

with col3:

    nextB = st.button('Next Topic')
    if nextB:
        session_state['isNextButtonCLicked'] = True
        if int(session_state['topicIndexCount']) >= (len(searchList) - 1):
            session_state['topicIndexCount'] = 0
        else:
            session_state['topicIndexCount'] = session_state['topicIndexCount'] + 1
        session_state['topicSelected'] = search[searchList[session_state['topicIndexCount']]]
    else:
        session_state['isNextButtonCLicked'] = False

if session_state['topicSelected'] != '':
    # df = pd.DataFrame([topics[session_state['topicSelected']][:4]], columns=config['topic_columns'], index=[topics[session_state['topicSelected']][0]])
    # st.dataframe(df)
    # st.markdown('----')
    topics[session_state['topicSelected']][4].main(session_state['topicSelected'])
else:
    st.markdown('----')
    DefaultSession.main()
