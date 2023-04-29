from dotenv import load_dotenv
from chatgpt_logger import logger
import openai
import os



def get_openai_options():
    openai_model = os.environ.get("OPENAI_MODEL")
    openai_temperature = os.environ.get("OPENAI_TEMPERATURE")
    oepnai_max_token =os.environ.get("OPENAI_MAX_TOKEN") 

    args = {
        'model': openai_model,
        'temperature' : openai_temperature,
        'max_token' : oepnai_max_token,
    }

    return args

def load_env():

    # set environment for application
    load_dotenv()
    version = os.environ.get("VERSION")
    openai_token = os.environ.get("OPENAI_TOKEN")

    version = os.environ.get("VERSION")

    # set openai connection
    openai.api_key=openai_token

    logger.info(f"app version :  {version} \t")


def answer_from_chatgpt(query):
    #query = 'yarn cluster manager의 개념을 알려줘'
    answer = ''
    if query is None or len(query) < 1:
        answer = 'No Response..'
        return answer


    options = get_openai_options()
    response = openai.Completion.create(model=options['model'], prompt=query, temperature=float(options['temperature']),max_tokens= int(options['max_token']))
    res = response['choices'][0]['text']
#    print(res)
    answer = res
    # for line in res.split("\n"):
    #     #print(line)
    #     answer = line
    
    return answer

    