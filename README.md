# MCQ-Generator-by-Gemini-Pro
Building end to end MCQ generator application using google gemini pro LLM model

Create a conda virtual enviroment and activate it
```bash
conda create -n MCQ_Generator python==3.9 -y
conda activate MCQ_Generator
```
Install all the requirements
```bash
python -m pip install -r requirements.txt
```
Get the Google API Key and Save into .env file
```bash
GOOGLE_API_KEY="............................."
```
TO Run the Application
```bash
python -m streamlit run app.py
```

### Techstack:
1. Python
2. Langchain
3. Streamlit
4. GenAI