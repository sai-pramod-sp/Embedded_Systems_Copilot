import string
import const
import boto3
from langchain.llms import Bedrock
import Constprompts
from langchain.prompts import PromptTemplate
import llama3
import os
from langchain.chains import LLMChain, SequentialChain

aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
region_name = os.getenv("region_name")


bedrock_llm = Bedrock(
    client=boto3.client(
        service_name = "bedrock-runtime", 
        region_name = region_name,
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key),
    model_id="meta.llama3-8b-instruct-v1:0"# Replace with your actual model ID
)

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

    CUSTOM_SYSTEM_PROMPT = Constprompts.Pipeline_Code_Generation1
    SYSTEM_PROMPT=const.B_SYS+CUSTOM_SYSTEM_PROMPT+const.E_SYS
    code_template=const.B_INST+SYSTEM_PROMPT+instruction+const.E_INST

    CUSTOM_SYSTEM_PROMPT1 = Constprompts.Pipeline_Test_Case_Generation2
    SYSTEM_PROMPT1=const.B_SYS+CUSTOM_SYSTEM_PROMPT1+const.E_SYS
    Test_template=const.B_INST+SYSTEM_PROMPT1+instruction+const.E_INST

    ''' 
    Creating Chain of Templates: First template is for generating the code
    Second template is to generate the Test_Cases for the generated in the 
    template1
    '''
    code_template = PromptTemplate(
        input_variables = ["task_description", "language"], 
        template = code_template
    )
    # code_prompt = code_template.format(task_description=input_text, language=language)
    
    code_chain = LLMChain(llm=bedrock_llm, prompt=code_template, verbose=True, output_key="code")

    test_code_template = PromptTemplate(
        input_variables = ["code"], 
        template=Test_template
    )

    test_Chain = LLMChain(
        llm=bedrock_llm,
        prompt=test_code_template, 
        output_key="test_cases",
        verbose=True
    )

    chain = SequentialChain(
        chains=[code_chain, test_Chain],
        input_variables=["task_description", "language"],
        output_variables=["test_cases"]
    )

    output = chain({"task_description":input_text, "language":language})
    cleaned_output = output["test_cases"]
    return cleaned_output

