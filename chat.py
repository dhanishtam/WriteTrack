from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def chat(inp, message_history, role="user"):
    client = OpenAI()
    message_history=[]
    message_history.append({"role": role, "content": f"{inp}"})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return reply_content