import streamlit as st
import time
# Set the page configuration
st.set_page_config(page_title="MCQs Creater App", 
                   page_icon="🧐", 
                   layout="centered", 
                   initial_sidebar_state="auto", 
                   )
from src.helper import llm_chain
from src.data_util import read_input_file
from src.logger import logging

# Set the page title
st.title(':red[MCQ] :blue[Generator]')
st.caption('                By :orange[Gemini-Pro] using Langchain 🐦')

with st.sidebar:
    # uploading the input file
    uploaded_file = st.file_uploader("Choose a PDF | Text file", 
                                    accept_multiple_files=False,
                                    type=['txt','pdf']
                                    )
    
    # Number of mcq questions user wants
    number = st.number_input("Insert a number", 
                             min_value= 1,
                             max_value= 50,
                            value=5, placeholder="Type a number...")

    # Difficulty level slider
    level = st.select_slider('Select difficulty',
                            options=['Easy', 'Medium', 'Hard'])

    if uploaded_file and number and level:
        data = read_input_file(uploaded_file)
        gen_button = st.button("Generate", key="gen_button")

try:
    if gen_button:
        with st.spinner('Generating Multi Choice Questions...'):
            # Generating the response from the model
            response = llm_chain.run(number = number,
                                    difficulty = level,
                                    text = data)
            # print(response)
        logging.info('MCQ are generated')
except NameError:
    pass
try:
    if gen_button and response:
        # write to UI
        message_placeholder = st.empty()
        full_response = ""
        for chunk in response.replace('\n','  \n').replace('\t','----'):
            full_response += chunk
            time.sleep(0.005)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        # st.markdown(response)
except NameError:
    pass