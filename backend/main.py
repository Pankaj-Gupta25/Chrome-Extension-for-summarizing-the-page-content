from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.document_loaders import PlaywrightURLLoader , WebBaseLoader
from langchain_core.documents import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class RequestModel(BaseModel):
    url: str

@app.get('/')
def home():
    return {'message':'home'}

@app.post("/summarize")
async def summarize_page(req: RequestModel):
    try:
        url = req.url

        loader = WebBaseLoader(url)
        docs = loader.load()

        if not docs:
            return {"summary": "No content found at the URL."}

        page_text = docs[0].page_content

        llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="openai/gpt-oss-20b"
        )

        chain = load_summarize_chain(llm, chain_type="stuff")
        summary = chain.run([Document(page_content=page_text)])

        return {"summary": summary}

    except Exception as e:
        return {"summary": f"Error: {str(e)}"}
