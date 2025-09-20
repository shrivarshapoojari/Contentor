from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


class GroqLLM:
    def __init__(self):
        load_dotenv()

    
    def get_llm(self):
        try:
            os.environ["GROQ_API_KEY"] = self.groq_api_key= os.getenv("GROQ_API_KEY")
            llm = ChatGroq(model="openai/gpt-oss-20b")
            return llm
        except Exception as e:
            print(f"Error initializing Groq LLM: {e}")
            return None