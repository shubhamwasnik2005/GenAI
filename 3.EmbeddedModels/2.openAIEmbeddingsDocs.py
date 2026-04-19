from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
os.environ["SSL_CERT_FILE"] = certifi.where()
embedding = OpenAIEmbeddings(
    model = "text-embedding-3-small",
    dimensions=32
)

docs = [
    "Mumbai is capital of maharashtra",
    "delhi is capital of india",
    "paris is capital of france"
]

result = embedding.embed_documents(docs)

print(str(result))