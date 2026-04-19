from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
os.environ["SSL_CERT_FILE"] = certifi.where()

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)


result = embeddings.embed_query("what is capital of india?")

print(str(result))