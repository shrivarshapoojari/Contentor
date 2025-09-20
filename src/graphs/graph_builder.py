from langgraph.graph import StateGraph,START,END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def  __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)
    

    def build_topic_graph(self):
        self.blog_node=BlogNode(self.llm)
        self.graph.add_node("title",self.blog_node.title)
        self.graph.add_node("content",self.blog_node.content)

        self.graph.add_edge(START,"title")
        self.graph.add_edge("title","content")
        self.graph.add_edge("content",END)

        return self.graph.compile()
    

    def setup_graph(self,usecase):

        if usecase=="topic":
            return self.build_topic_graph()