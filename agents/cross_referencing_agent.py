import os
from typing import List
from langchain_core.runnables import RunnableSequence, RunnablePassthrough
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI

class CrossReferencingAgent:
    """
    A class to represent an agent that cross-references articles using OpenAI's GPT-4.

    Attributes:
        llm: An instance of OpenAI for cross-referencing articles.
        prompt: A prompt template for cross-referencing.
        chain: A chain for executing the cross-referencing task.
    """

    def __init__(self, openai_api_key: str):
        """
        Initializes the CrossReferencingAgent with the provided OpenAI API key.

        Args:
            openai_api_key (str): The API key for OpenAI.
        """
        self.llm = OpenAI(model_name="gpt-4", temperature=0, openai_api_key=openai_api_key)
        
        self.prompt = PromptTemplate(
            input_variables=["article", "related_topics"],
            template="Cross-reference the following article with related topics:\n\nArticle: {article}\n\nRelated Topics: {related_topics}\n\nProvide verification and additional insights."
        )
        
        self.chain = RunnableSequence(
            RunnablePassthrough() | self.prompt | self.llm | StrOutputParser()
        )

    def verify_and_enhance(self, article: str, related_topics: List[str]):
        """
        Verifies and enhances the provided article with related topics.

        Args:
            article (str): The article to verify and enhance.
            related_topics (List[str]): A list of related topics for cross-referencing.

        Returns:
            str: The enhanced information based on the cross-referencing.
        """
        response = self.chain.invoke({"summary": article, "topics": related_topics})
        return response

# Example Usage
if __name__ == "__main__":
    cross_ref = CrossReferencingAgent(openai_api_key=os.getenv("OPENAI_API_KEY"))
    enhanced_info = cross_ref.verify_and_enhance("Article text here.", ["AI Ethics", "Regulatory Compliance"])
    print(enhanced_info)
