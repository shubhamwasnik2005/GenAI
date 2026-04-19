from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

# Fix SSL issue
os.environ["SSL_CERT_FILE"] = certifi.where()
model = ChatOpenAI(model='gpt-4')

response = model.invoke("suggest me 20 indian boys names?")

print(response.content)

