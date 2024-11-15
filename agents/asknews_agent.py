import os
from asknews_sdk import AskNewsSDK
from langchain_community.tools.asknews import AskNewsSearch
from pydantic import BaseModel
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.retrievers import AskNewsRetriever
from .base_agent import BaseAgent

class AskNewsAgent(BaseAgent):
    """
    A class to represent an agent that fetches news articles using the AskNews API.
    """

    def __init__(self, client_id: str, client_secret: str):
        super().__init__()
        self.client = AskNewsSDK(client_id=client_id, client_secret=client_secret)
        self.retriever = AskNewsRetriever(k=10)

    def fetch_news(self, query: str):
        """
        Fetches news articles based on a query.
        """
        try:
            docs = self.retriever.invoke(query)
            news_articles = [doc.page_content for doc in docs]
            return news_articles
        except Exception as e:
            print(f"Error fetching news: {e}")
            return []
