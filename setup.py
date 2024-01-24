from setuptools import find_packages,setup

setup(
    name='mcq-generator',
    version='0.0.1',
    author='elavala srinivas reddy',
    author_email='elavalasrinivasreddy@gmail.com',
    install_requires=['google-generativeai',
                      'langchain',
                      'streamlit',
                      'python-dotenv',
                      'PyPDF2'],
    packages=find_packages()
)