from src.logger import logging
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from src.few_show_prompt import mcq_prompt

# initiating the env variables
load_dotenv()

# Reading API KEY
GOOGLE_API_KEY = os.getenv("API_KEY")
logging.info(f'GOOGLE API KEY is {GOOGLE_API_KEY}')

@st.cache_resource
def create_llm_model():
    # Creating LLM model
    return ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY,
                                    model="gemini-pro",
                                    temperature=0.3,
                                    )
llm_model = create_llm_model()
logging.info('LLM model object is created...')

# Creating chain from langchain
llm_chain = LLMChain(llm=llm_model,
                      prompt=mcq_prompt,
                      output_key="mcq",
                      verbose=False,
                      )
logging.info('Base chain was created...')
