from dotenv import load_dotenv
import os
load_dotenv()

# Use the local model to
from ollama import Client
client = Client(host='http://localhost:11434')

def generate(prompt):
    response = client.generate(model='mistral', prompt=prompt)
    return response['response']