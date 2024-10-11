import streamlit as st
import torch
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM
import llama3
import Constprompts
import string

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<>\n", "\n<>\n\n"

strings_to_replace = ["[INST]", "[/INST]", "<>\n", "\n<>\n\n", "<INST>"]

def remove_punc(text):
    exclude = string.punctuation
    return text.translate(str.maketrans("", "", exclude))

def replace_strings_with_space(text, strings_to_replace):
    for string in strings_to_replace:
        text = text.replace(string, ' ')
    return text

def getLLamaresponse(input_text,language,blog_style):

    instruction = input_text

    if(blog_style == 'To Generate the Code'):
        
        CUSTOM_SYSTEM_PROMPT = Constprompts.Generation
        SYSTEM_PROMPT=B_SYS+CUSTOM_SYSTEM_PROMPT+E_SYS
        template=B_INST+SYSTEM_PROMPT+instruction+E_INST
    
        prompt=PromptTemplate(input_variables=["language", "task_description"], template=template)
        formatted_prompt = prompt.format(language=language, task_description=input_text)

    elif (blog_style == 'Optimize the Code'):

        CUSTOM_SYSTEM_PROMPT = Constprompts.Optimization
        SYSTEM_PROMPT=B_SYS+CUSTOM_SYSTEM_PROMPT+E_SYS
        template=B_INST+SYSTEM_PROMPT+instruction+E_INST
    
        prompt=PromptTemplate(input_variables=["language", "task_description"], template=template)
        formatted_prompt = prompt.format(language=language, task_description=input_text)

    elif (blog_style == 'Generate the Suggestion'):

        CUSTOM_SYSTEM_PROMPT = Constprompts.Text_Generation
        SYSTEM_PROMPT=B_SYS+CUSTOM_SYSTEM_PROMPT+E_SYS
        template=B_INST+SYSTEM_PROMPT+instruction+E_INST

        prompt=PromptTemplate(input_variables=["task_description"], template=template)
        formatted_prompt = prompt.format(task_description=input_text)

    else:

        CUSTOM_SYSTEM_PROMPT = Constprompts.Test_Case_Generation
        SYSTEM_PROMPT=B_SYS+CUSTOM_SYSTEM_PROMPT+E_SYS
        template=B_INST+SYSTEM_PROMPT+instruction+E_INST
    
        prompt=PromptTemplate(input_variables=["language", "task_description"], template=template)
        formatted_prompt = prompt.format(language=language, task_description=input_text)
    

    return_output = llama3.code_generate(formatted_prompt)
    return return_output

# Set page configuration
st.set_page_config(
    page_title="Embedded Systems",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# Header
st.header("Embedded System AI Assistant ")


# Text input with tooltip
input_text = st.text_input("Ask me Anything", help="Type your query here")

# Columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    language = st.selectbox('Select Language', ('C', 'C++', 'None'), index=0, help="Choose the programming language")
with col2:
    blog_style = st.selectbox('Help assistant for', ('To Generate the Code', 'Optimize the Code', 'Testing the Code', 'Generate the Suggestions'), index=0, help="Select the type of assistance you need")

# Button to generate response with loading indicator
submit = st.button("Generate")
if submit:
    with st.spinner('Processing...'):
        output = getLLamaresponse(input_text, language, blog_style)
        cleaned_output = replace_strings_with_space(output, strings_to_replace)
        st.write(cleaned_output)

# Feedback section
st.sidebar.header("Feedback")
feedback = st.sidebar.text_area("Your feedback", help="Let us know your thoughts or report issues")
if st.sidebar.button("Submit Feedback"):
    st.sidebar.write("Thank you for your feedback!")