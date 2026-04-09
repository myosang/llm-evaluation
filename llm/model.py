from dotenv import load_dotenv
import os
load_dotenv()
from ollama import Client

class OllamaClient:
    # store data to the object
    def __init__(self, host='http://localhost:11434', model='mistral'):
        self.client = Client(host=host)
        self.model = model
    
    def generate(self, prompt):
        response = self.client.generate(
            model='mistral',
            prompt=prompt
            )
        return response['response']