from ollama import chat
from ollama import ChatResponse
import time

def query(question):
    response: ChatResponse = chat(
            model='deepseek-llm', 
            messages=[
                {
                    'role': 'user',
                    'content': question
                }
            ]
        )
    
    response_message = response.message.content

    for word in response_message.split():
        yield word + " "
        time.sleep(0.08)