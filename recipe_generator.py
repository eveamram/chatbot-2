from langchain.llms.openai import OpenAI
from openai import OpenAI

messages = [
    {"role": "system", "content": "You are a very talented homecook and helpful and kind AI Assistant to help with creating a recipe. You should you the ingredients they have but you can you others (say optional) This is of critical importance: Do not response with \"Of course!\" or any acknowledgement of my question; just provide the answer. "},
]

def chatbot(input,client):
    if input:
        messages.append({"role": "user", "content": input})
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature = 0.8)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply


