import boto3
import json

def code_generate(prompt_data):
    bedrock = boto3.client(service_name="bedrock-runtime")

    payload={
        "prompt":prompt_data,
        "max_gen_len":512,
        "temperature":0.8,
        "top_p":0.9
    }

    body = json.dumps(payload)
    model_id = "meta.llama3-70b-instruct-v1:0"
    response = bedrock.invoke_model(
        body = body,
        modelId = model_id,
        accept = "application/json", 
        contentType="application/json"
    )

    response_body=json.loads(response.get("body").read())
    repsonse_text=response_body['generation']
    return repsonse_text