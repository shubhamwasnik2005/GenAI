from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
os.environ["SSL_CERT_FILE"] = certifi.where()

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

docs = [
    "Mumbai is capital of maharashtra",
    "delhi is capital of india",
    "paris is capital of france"
]

result = embeddings.embed_documents(docs)

print(str(result))