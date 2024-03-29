from chatgpt_service import load_env,answer_from_chatgpt
from chatgpt_logger import logger
import streamlit as st



def send_callback():
    query = st.session_state['query']
    answer = answer_from_chatgpt(query)
    st.session_state['answer'] = answer

def clear_callback():
     st.session_state.clear()
def load_streamlit():
    #st.sidebar.text_input ='test'
    title = st.title = '## Chat GPT Simple Application .. :robot_face:'
    st.sidebar.title('MyGPT')

    st.write(title)
    st.text_input('prompt:keyboard:',key='query')



    
    col1,col2,col3 = st.columns([1,1,1])
    with col1:
        st.button("send",on_click=send_callback)
    with col3:
        st.button("clear",on_click=clear_callback)
    
    st.text_area('response',key='answer',height=500)
    
    

    
    
    
    
    
    


def main():
    logger.info("main application start..")
    load_env()
    load_streamlit()
    #answer_from_chatgpt("지금 시간은?")

if __name__=='__main__':
    main()