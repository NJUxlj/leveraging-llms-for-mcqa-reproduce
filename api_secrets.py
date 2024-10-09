
import os

def get_api_key_by_name(name):
    return {
        "openai": os.environ["OPENAI_API_KEY"],  # Add your key here
        "jurassic": os.environ["JURASSIC_KEY"],  # Add your key here
        "chatglm": os.environ["CHATGLM_KEY"],
    }[name]
    
    
# https://studio.ai21.com/account/api-key   for Jurassic

