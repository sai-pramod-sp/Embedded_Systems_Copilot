import streamlit as st
import torch
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM
import llama3
import Constprompts
import string

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<>\n", "\n<>\n\n"


def remove_punc(text):
    exclude = string.punctuation
    return text.translate(str.maketrans("", "", exclude))

def getLLamaresponse(input_text,language,blog_style):

    instruction = input_text

    if(blog_style == 'To Generate the Code'):
        
        CUSTOM_SYSTEM_PROMPT = Constprompts.Generation
        

    elif (blog_style == 'Optimize the Code'):

        CUSTOM_SYSTEM_PROMPT = Constprompts.Optimization

    else:

        CUSTOM_SYSTEM_PROMPT = Constprompts.Test_Case_Generation
    
    
    SYSTEM_PROMPT=B_SYS+CUSTOM_SYSTEM_PROMPT+E_SYS
    template=B_INST+SYSTEM_PROMPT+instruction+E_INST
    
    prompt=PromptTemplate(input_variables=["language", "task_description"], template=template)
    formatted_prompt = prompt.format(language=language, task_description=input_text)

    return_output = llama3.code_generate(formatted_prompt)
    return return_output

st.set_page_config(page_title="Embedded Systems",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Embedded System AI Assistant 🤖")

input_text = remove_punc(st.text_input("Ask me Anything"))

## creating to more columns for additonal 2 fields
col1,col2=st.columns([5,5])

with col1:
    language=st.selectbox('Select Language',
                            ('C','C++'),index=0)
with col2:
    blog_style=st.selectbox('Help assistant for',
                            ('To Generate the Code','Optimize the Code','Testing the Code'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,language,blog_style))