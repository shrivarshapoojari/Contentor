import uvicorn
from fastapi import FastAPI,Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM
import os
from dotenv import load_dotenv

load_dotenv()

app=FastAPI()

langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key is not None:
    os.environ["LANGSMITH_API_KEY"] = langchain_api_key



@app.post("/blogs")
async def create_blog(request:Request):
    body=await request.json()
    topic=body.get("topic","")
    llm=GroqLLM().get_llm()
    graph_builder=GraphBuilder(llm)

    if topic and llm:
        graph=graph_builder.setup_graph(usecase="topic")
        state=graph.invoke({"topic":topic})
         
    
    return  {"data":state}


if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0",port=8000,reload=True)


 