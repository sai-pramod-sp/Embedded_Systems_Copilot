import string
import const
import Constprompts
from langchain.prompts import PromptTemplate
import llama3

def remove_punc(text):
    exclude = string.punctuation
    return text.translate(str.maketrans("", "", exclude))

def replace_strings_with_space(text):
    for string in const.strings_to_replace:
        text = text.replace(string, ' ')
    return text

def getLLamaresponse(input_text,language,blog_style):

    instruction = input_text

    if(blog_style == 'To Generate the Code'):
        
        CUSTOM_SYSTEM_PROMPT = Constprompts.Generation
        SYSTEM_PROMPT=const.B_SYS+CUSTOM_SYSTEM_PROMPT+const.E_SYS
        template=const.B_INST+SYSTEM_PROMPT+instruction+const.E_INST
    
        prompt=PromptTemplate(input_variables=["language", "task_description"], template=template)
        formatted_prompt = prompt.format(language=language, task_description=input_text)

    elif (blog_style == 'Optimize the Code'):

        CUSTOM_SYSTEM_PROMPT = Constprompts.Optimization
        SYSTEM_PROMPT=const.B_SYS+CUSTOM_SYSTEM_PROMPT+const.E_SYS
        template=const.B_INST+SYSTEM_PROMPT+instruction+const.E_INST
    
        prompt=PromptTemplate(input_variables=["language", "task_description"], template=template)
        formatted_prompt = prompt.format(language=language, task_description=input_text)

    elif (blog_style == 'Generate the Text'):

        CUSTOM_SYSTEM_PROMPT = Constprompts.Text_Generation
        SYSTEM_PROMPT=const.B_SYS+CUSTOM_SYSTEM_PROMPT+const.E_SYS
        template=const.B_INST+SYSTEM_PROMPT+instruction+const.E_INST

        prompt=PromptTemplate(input_variables=["task_description"], template=template)
        formatted_prompt = prompt.format(task_description=input_text)

    elif (blog_style == 'Testing the Code'):

        CUSTOM_SYSTEM_PROMPT = Constprompts.Test_Case_Generation
        SYSTEM_PROMPT=const.B_SYS+CUSTOM_SYSTEM_PROMPT+const.E_SYS
        template=const.B_INST+SYSTEM_PROMPT+instruction+const.E_INST
    
        prompt=PromptTemplate(input_variables=["language", "task_description"], template=template)
        formatted_prompt = prompt.format(language=language, task_description=input_text)
    

    return_output = llama3.code_generate(formatted_prompt)
    return return_output

# Creating Chain (For reference: https://github.com/sai-pramod-sp/Gen-AI/blob/main/Complete_Langchain.ipynb)
def getCode(input_text, language): 

    instruction = input_text

    CUSTOM_SYSTEM_PROMPT = Constprompts.Pipeline_Test_Case_Generation
    SYSTEM_PROMPT=const.B_SYS+CUSTOM_SYSTEM_PROMPT+const.E_SYS
    template=const.B_INST+SYSTEM_PROMPT+instruction+const.E_INST

    code_template = PromptTemplate(
        input_variables = ["task_description", "language"], 
        template = template
    )
    code_prompt = code_template.format(task_description=input_text, language=language)
    code = llama3.code_generate(code_prompt)
    
    return code