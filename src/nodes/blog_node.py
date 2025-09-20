from src.states.blogstate import BlogState


class BlogNode:


    def __init__(self,llm):
        self.llm=llm
    


    def title(self,state:BlogState):

        if "topic" in state and state["topic"]:
            prompt="""You are an expert blog content writer.Use Markdown formatting to create a catchy and engaging blog title based on the given topic.
            Topic: {topic}.
            The  title should be concise, attention-grabbing, and relevant to the topic.
            Ensure the title is unique and stands out to attract readers.
            Return only the title without any additional text or punctuation.
          """
            
            system_message=prompt.format(topic=state["topic"])

            response=self.llm.invoke(system_message)
            
            return{"blog":{"title":response.content}}
