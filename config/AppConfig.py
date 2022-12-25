from sessions import Session1StreamlitHellowWorld, Session3StreamlitTitle, Session2StreamlitTextElementsSideBar, Session4StreamlitCheckbox, Session6StreamlitRadioButton, \
    Session5StreamlitHerokuDeployment

config = dict()
config['topic_columns'] = ['Topic ID', 'Session', 'Title', 'Date']

search = dict()
search['Session-1 Introduction Installation and HelloWorld'] = 'Python install streamlit  pip install streamlit streamlit hello activate deactivate conda activate conda deactivate pyCharm IDE'
search['Session-2 Streamlit Text Elements and Sidebar'] = 'Streamlit title, header, subheader, text, write, markdown, code, caption, latex and sidebar'
search['Session-3 Streamlit Title Elements'] = 'Streamlit Title Elements'
search['Session-4 Streamlit Checkbox (Basics and Advance Features)'] = 'Streamlit Checkbox, basics and advance features'
search['Session-5 Streamlit App : Deployment on Heroku Cloud'] = 'How do we deploy Streamlit applications on Heroku?'
# search['Session-6 Streamlit Radio (Basics and Advance Features)'] = 'Streamlit Radio, basics and advance features'
topics = dict()
topics['Session-1 Introduction Installation and HelloWorld'] = [1, 'Session-1', 'Installation Introduction and HelloWorld', '31-01-2022', Session1StreamlitHellowWorld]
topics['Session-2 Streamlit Text Elements and Sidebar'] = [2, 'Session-2', 'Streamlit Text Elements and Sidebar', '03-02-2022', Session2StreamlitTextElementsSideBar]
topics['Session-3 Streamlit Title Elements'] = [3, 'Session-3', 'Streamlit Title Elements', '04-05-2022', Session3StreamlitTitle]
topics['Session-4 Streamlit Checkbox (Basics and Advance Features)'] = [4, 'Session-4', 'Streamlit Checkbox Basics and Advance Features',  '03-07-2022', Session4StreamlitCheckbox]
topics['Session-5 Streamlit App : Deployment on Heroku Cloud'] = [5, 'Session-5', 'How do we deploy Streamlit applications on Heroku?', '17-12-2022', Session5StreamlitHerokuDeployment]
# topics['Session-6 Streamlit Radio (Basics and Advance Features)'] = [5, 'Session-5', 'Streamlit Radio Basics and Advance Features', '27-11-2022', Session6StreamlitRadioButton]
