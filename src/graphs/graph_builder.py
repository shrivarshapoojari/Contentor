from langgraph.graph import StateGraph,START,END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState


class GraphBuilder:
    def  __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)
    

    def build_topic_graph(self):
        
        self.graph.add_node("title",)
        self.graph.add_node("content",)

        self.graph.add_edge(START,"title")
        self.graph.add_edge("title","content")
        self.graph.add_edge("content",END)