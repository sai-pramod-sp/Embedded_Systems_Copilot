
import streamlit as st
import torch
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM


## Function To get response from LLAma 2 model

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<>\n", "\n<>\n\n"

def getLLamaresponse(input_text,language,blog_style):

    instruction = input_text
    model_name = "Meta-Llama-3.1-8B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Prompt Template
    CUSTOM_SYSTEM_PROMPT = """
        Generate a {language} code sample for an embedded system. The code should perform the following task: {task_description}.
               """
    SYSTEM_PROMPT=B_SYS+CUSTOM_SYSTEM_PROMPT+E_SYS
    template=B_INST+SYSTEM_PROMPT+instruction+E_INST
    
    prompt=PromptTemplate(input_variables=["language", "task_description"], template=template)

    # Initializing the Chain
    # LLM_Chain=prompt.format(llm=model, prompt=prompt)
    formatted_prompt = prompt.format(language=language, task_description=input_text)

    # inputs = tokenizer(input_text, return_tensors="pt")
    # outputs = model.generate(**inputs)

    # response = (tokenizer.decode(outputs[0], skip_special_tokens=True))
    inputs = tokenizer(formatted_prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=500, num_return_sequences=1)

    # Decode the output tokens
    predicted_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return predicted_text

st.set_page_config(page_title="Embedded Systems",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Embedded System AI Assistant 🤖")

input_text=st.text_input("Ask me Anything")

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