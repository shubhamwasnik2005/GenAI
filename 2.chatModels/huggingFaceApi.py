from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
os.environ["SSL_CERT_FILE"] = certifi.where()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.7",
    task="text-generation",
    temperature=0.5,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")

print(response.content)