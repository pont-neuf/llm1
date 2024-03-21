from transformers import pipeline
pipe = pipeline("text-generation",model="mistralai/Mistral-7B-Instruct-v0.2")

print(pipe)


