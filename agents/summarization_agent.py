import os
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI


class SummarizationAgent:
    """
    Agent for generating brief, mid-length, and enhanced summaries.
    """

    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model_name="gpt-4",
            temperature=0.7
        )

        # Define prompts
        self.small_tldr_prompt = ChatPromptTemplate.from_template(
            "Provide a brief summary (1-2 sentences) of the following article:\n\n{summary}"
        )
        self.mid_tldr_prompt = ChatPromptTemplate.from_template(
            "Provide a concise summary (one paragraph) of the following article:\n\n{summary}"
        )
        self.enhanced_prompt = ChatPromptTemplate.from_template(
            "Enhance this summary with additional insights:\n\n{summary}"
        )

    def generate_summaries(self, summary):
        """
        Generate brief, mid-length, and enhanced summaries for a given text.

        Args:
            summary (str): The text to summarize.

        Returns:
            dict: A dictionary with three types of summaries.
        """
        return {
            "small_tldr": self.llm.predict(self.small_tldr_prompt.format(summary=summary)),
            "mid_tldr": self.llm.predict(self.mid_tldr_prompt.format(summary=summary)),
            "enhanced_summary": self.llm.predict(self.enhanced_prompt.format(summary=summary)),
        }