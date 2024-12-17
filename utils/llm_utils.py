import os
import json
import requests
from groq import Groq

def get_llm_output(prompt, temperature=0.7, max_tokens=4096):
    model_params = {
        "max_tokens": max_tokens,
        "temperature": temperature,
        "model": "gpt-4"
    }
    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )   
    completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
                "content": prompt,
        }
    ],
    model="llama-3.3-70b-versatile",
    temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        stop=None,
    )
    out = completion.choices[0].message.content
    print("llm output: ", out)
    return out
# if __name__ == "__main__":
#     get_llm_output('Write me a love poem about tintin and chang')
