from fastapi import FastAPI
from transformers import pipeline 

app = FastAPI()

@app.post("/chat")
async def chat(data: dict):
    chat = [
        {"role":"system","content":"You are a doctor who diagnosis patients based on their symptoms."},
        {"role":"user","content":f"{user_input}"}
    ]
    pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-1.7B-Instruct",model_kwargs={"use_cache": True})
    response = pipe(chat, max_new_tokens=512)
    return {"response":response}