from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

# Fix SSL issue
os.environ["SSL_CERT_FILE"] = certifi.where()

llm = ChatOpenAI(model="gpt-4.1-mini")

response = llm.invoke("What is the capital of India?")

print(response.content)