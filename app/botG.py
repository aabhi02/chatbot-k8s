import time
import ollama

def query(question):
    # client = ollama.Client(host="http://localhost:46151/")
    client = ollama.Client(host="http://ollama.ollama.svc.cluster.local:11434")
    
    response = client.chat(
            model='deepseek-r1:1.5b', 
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


from groq import Groq

client = Groq(
    api_key="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",
)

def querygroq(question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gemma2-9b-it",
    )

    response_message = chat_completion.choices[0].message.content

    for word in response_message.split():
        yield word + " "
        time.sleep(0.08)
