import os
from pymongo import MongoClient
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from dotenv import load_dotenv
load_dotenv(override=True)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MONGO_URI = os.environ.get("MONGO_VECTOR_URI")
DB_NAME = "krayonsdb"
COLLECTION_NAME = "bigtech"

embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

def generate_embedding(text):
    response = embeddings.embed_query(text)
    embedding = response['data'][0]['embedding']
    return embedding

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

for document in collection.find():
    text = document["data"]  # Adjust field name as necessary
    embedding = generate_embedding(text)
    collection.update_one({"_id": document["_id"]}, {"$set": {"embedding": embedding}})

def rag_query(query):
    vector_search = MongoDBAtlasVectorSearch.from_connection_string(
      MONGO_URI,
      DB_NAME + "." + COLLECTION_NAME,
      embeddings,
      index_name="vector_index"
    )
    results = vector_search.similarity_search(
      query=query,
      k=20
    )
    
    return results
  
print(rag_query("What is MongodB?"))

