from fastapi import FastAPI, Form
# from rag import rag_query

app = FastAPI()

@app.post("/query/")
async def query_llm(query: str = Form(...)):
    # response = rag_query(query)
    return {"llm_response": query}
