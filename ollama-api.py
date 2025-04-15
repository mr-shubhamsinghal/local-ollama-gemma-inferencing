from fastapi import FastAPI
from ollama import Client
from fastapi import Body

app = FastAPI()
client = Client(
    host='http://localhost:11434'
)

model = 'gemma3:1b'
client.pull(model)

@app.post('/chat')
def chat(message: str = Body(..., description="Chat Message")):
    response = client.chat(
        model=model,
        messages=[
            { "role": "user", "content": message }
        ]
    )
    print(response)
    return response['message']['content']
