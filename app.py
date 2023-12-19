from assignment2 import ExtractDrugNames
from model import TestFunction
import streamlit as st

# ---------------------------------------------------------------------------------

st.title('Syed Raheel Ahmed (21K-4198)')
st.title('NLP Assignments Demo')
st.title('------------------------------------------')

# ----------------------------------------------------------------------------------

st.header('Assignment 2 (Extract Drugs)')

text = st.text_area('Enter Text to Extract Drugs from')
button1 = st.button('Extract Drugs')

if text and button1:
    drugs = ExtractDrugNames(text)
    if drugs:
        st.success(drugs)
    else:
        st.success('Sorry, No Drugs Found')

# ------------------------------------------------------------------------------------------------

st.title('------------------------------------------')
st.header('Assignment 4 (Classify Documents)')
st.write('Classify Documents of following subjects \n 1) Machine Learning \n 2) Deep Learning \n 3) Computer Vision \n 4) Natural Language Processing \n5) Nature Insipired Iterative Algorithms')

uploaded_file = st.file_uploader("Choose a PDF file", type = 'pdf')
button2 = st.button('Submit')

if uploaded_file and button2 :
    result = TestFunction(uploaded_file)
    
    if result == 'NIIA':
        st.success(f'Document belongs to category of Nature Inspired Iterative Algorithm', icon="✅")
    
    if result == 'CV':
        st.success(f'Document belongs to category of Computer Vision', icon="✅")
        
    if result == 'DL':
        st.success(f'Document belongs to category of Deep Learning', icon="✅")
        
    if result == 'ML':
        st.success(f'Document belongs to category of Machine Learning', icon="✅")
        
    if result == 'NLP':
        st.success(f'Document belongs to category of Natural Language Processing', icon="✅")
        
st.title('------------------------------------------')