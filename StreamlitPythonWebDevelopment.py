import pandas as pd
import streamlit as st
from streamlit import session_state

from sessions import DefaultSession
from PIL import Image
from config.AppConfig import topics, config, search

searchValuesList = list(search.values())
searchList = list(search.keys())
if 'topicIndexCount' not in session_state.keys():
    session_state['topicIndexCount'] = 0
if 'isNextButtonCLicked' not in session_state.keys():
    session_state['isNextButtonCLicked'] = False
if 'isPrevButtonCLicked' not in session_state.keys():
    session_state['isPrevButtonCLicked'] = False
if 'topicSelected' not in session_state.keys():
    session_state['topicSelected'] = ''
if 'topicDropdownSelected' not in session_state.keys():
    session_state['topicSelected'] = searchList[0]
    session_state['topicDropdownSelected'] = search[str(session_state['topicSelected'])]
if 'chkPageSelected' not in session_state.keys():
    session_state['chkPageSelected'] = ''

def update_prev_button():
    session_state['isNextButtonCLicked'] = False
    session_state['isPrevButtonCLicked'] = True
    if int(session_state['topicIndexCount']) <= 0:
        session_state['topicIndexCount'] = len(searchList) - 1
    else:
        session_state['topicIndexCount'] = session_state['topicIndexCount'] - 1
    session_state['topicSelected'] = searchList[session_state['topicIndexCount']]
    session_state['topicDropdownSelected'] = search[str(session_state['topicSelected'])]


def get_index_topi(value):
    index = 0
    if value is None or value == '':
        return index
    else:
        for key in search.keys():
            if value == search[key]:
                return index
            index += 1

    return index


def update_selection_change():
    countSelected = get_index_topi(session_state['whenClicked'])
    session_state['topicIndexCount'] = countSelected
    session_state['topicSelected'] = searchList[session_state['topicIndexCount']]
    session_state['topicDropdownSelected'] = search[searchList[session_state['topicIndexCount']]]


def update_next_button():
    session_state['isPrevButtonCLicked'] = False
    session_state['isNextButtonCLicked'] = True
    if int(session_state['topicIndexCount']) >= (len(searchList) - 1):
        session_state['topicIndexCount'] = 0
    else:
        session_state['topicIndexCount'] = session_state['topicIndexCount'] + 1
    session_state['topicSelected'] = searchList[session_state['topicIndexCount']]
    session_state['topicDropdownSelected'] = search[str(session_state['topicSelected'])]
image = Image.open('assets/python_techie_logo.PNG')

st.set_page_config(
    page_title='Streamlit Python Web Development',
    page_icon=image,
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                .css-1l40rdr { text-align: left;}
                .css-sc0g0 { text-align: center;}
                .css-18e3th9 { padding-top: 3%;}
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
                .css-1vq4p4l { padding: 3rem 1rem 1.5rem;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# st.title("Welcome to Streamlit-Python-Web")

st.header("Python - Learn - Grow - Fly - High")
if session_state['isPrevButtonCLicked'] or session_state['isNextButtonCLicked']:
    st.selectbox('Search Your Interest', searchValuesList, index=searchValuesList.index(session_state['topicDropdownSelected']), key='whenClicked', on_change=update_selection_change)
else:
    st.selectbox('Search Your Interest', searchValuesList, index=searchValuesList.index(session_state['topicDropdownSelected']), key='whenClicked', on_change=update_selection_change)

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    prev = st.button('Prev Topic', on_click=update_prev_button)
with col3:
    nextB = st.button('Next Topic', on_click=update_next_button)
print(session_state['topicSelected'])
print(session_state['topicIndexCount'])
if session_state['topicSelected'] != '':
    with st.sidebar:
        st.image(image, width=200)
        st.sidebar.title("Python-Streamlit")
        st.sidebar.markdown('''
            <small>This session Tutor [Javalingappa](https://www.linkedin.com/in/javalingappa/), 
            Follow my Channel on [Python Tchie - Youtube](https://www.youtube.com/channel/UCumeOi-LeRBGhVdzjXyAy1A),
            Download code here  [Github](https://github.com/javaindubai/streamlit-python-web-development/tree/s1_install_hellowworld).</small>
                ''', unsafe_allow_html=True)
    topics[session_state['topicSelected']][4].main(session_state['topicSelected'])
else:
    with st.sidebar:
        st.image(image, width=200)
        st.sidebar.title("Streamlit-Python-Web")
        st.sidebar.markdown('''
            <small>This session Tutor [Javalingappa](https://www.linkedin.com/in/javalingappa/), 
            Follow my Channel on [Python Tchie - Youtube](https://www.youtube.com/channel/UCumeOi-LeRBGhVdzjXyAy1A),
            Download code here  [Github](https://github.com/javaindubai/streamlit-python-web-development/tree/s1_install_hellowworld).</small>
                ''', unsafe_allow_html=True)

    session_state['topicIndexCount'] = searchList.index(session_state['whenClicked'])
    session_state['topicSelected'] = searchList[session_state['topicIndexCount']]
    topics[session_state['topicSelected']][4].main(session_state['topicSelected'])
