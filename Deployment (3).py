#!/usr/bin/env python
# coding: utf-8

# In[2]:
import pandas as pd
import streamlit as st 
from sklearn.tree import  DecisionTreeClassifier
from pickle import dump
from pickle import load

#change page name and icon
import streamlit as st
st.image("Excelr.jpeg")

# In[2]:


st.title('Model Deployment:Decision Tree Classifier')


# In[ ]:


st.sidebar.header('User Input Parameters')

def user_input_features():
    Hospital_Id = st.sidebar.number_input("Enter the hospital ID")
    Age = st.sidebar.selectbox('Age',('4','3','2','1','0'))
    Days_spend_hsptl = st.sidebar.number_input("Insert days spent")
    Home_or_selfcare = st.sidebar.number_input('Enter the code')
    ccs_diagnosis_code = st.sidebar.number_input('Enter the diadnosis code')
    ccs_procedure_code = st.sidebar.number_input('Enter the procedural code')
    apr_drg_description	= st.sidebar.number_input('Enter the drug description code')
    Code_illness = st.sidebar.selectbox('Code_illness',('0','1','2','3','4'))
    Surg_Description = st.sidebar.selectbox('Surg_Description',('0','1','2'))
    Tot_charg = st.sidebar.number_input("Insert the total charge")
    Tot_cost = st.sidebar.number_input("Insert the total cost")
    data = {'Hospital ID':Hospital_Id,
            'Age':Age,
            'Days_spend_hsptl':Days_spend_hsptl,
            'Home or self care':Home_or_selfcare,
            'ccs_diagnosis_code':ccs_diagnosis_code,
            'ccs_procedure_code':ccs_procedure_code,
            'drug description' :apr_drg_description,
            'Code_illness':Code_illness,
            'Surg_Description':Surg_Description,
            'Tot_charg':Tot_charg,
            'Tot_cost':Tot_cost}
    features = pd.DataFrame(data,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)


# In[ ]:


# load the model from disk
loaded_Model = load(open('Decision_Tree.sav', 'rb'))


# In[ ]:


prediction = loaded_Model.predict(df)


# In[ ]:


st.latex('Result: Genuine' if prediction==1 else 'Result: Fraud')



# In[ ]:
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")


                                                                   

