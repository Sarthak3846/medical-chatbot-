import torch
import transformers
from transformers import pipeline, BitsAndBytesConfig

while True:
    user_input = input("You: ")
    if user_input=="stop":
        break
    chat = [
        {"role":"system","content":"You are a doctor who diagnosis patients based on their symptoms."},
        {"role":"user","content":f"{user_input}"}
    ]
    pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-1.7B-Instruct",model_kwargs={"use_cache": True})
    response = pipe(chat, max_new_tokens=512)
    print(response[0]['generated_text'][-1]['content'])