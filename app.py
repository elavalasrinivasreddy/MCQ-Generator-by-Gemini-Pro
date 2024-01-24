import streamlit as st
# Set the page configuration
st.set_page_config(page_title="MCQs_GP", 
                   page_icon="random", 
                   layout="centered", 
                   initial_sidebar_state="auto", 
                   )
from src.helper import llm_chain
from src.data_util import read_input_file
from src.logger import logging

# Set the page title
st.title(':red[MCQ] :blue[Creater Application]')
st.caption('By :orange[Gemini-Pro] using Langchain')

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
        if st.button("Generate", type="primary"):
            with st.spinner('Generating Multi Choice Questions...'):
                # Generating the response from the model
                response = llm_chain.run(number = number,
                                        difficulty = level,
                                        text = data)
                print(response)
        try:
            if response:
                # write to UI
                st.markdown(response)
        except NameError:
            pass