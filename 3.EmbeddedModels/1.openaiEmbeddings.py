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

result = embedding.embed_query("what is the capital of india?")

print(str(result))