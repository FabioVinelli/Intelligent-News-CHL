"""
Custom state class for managing conversation summaries and messages.
"""

from langgraph.graph import MessagesState


class NewsState(MessagesState):
    """
    A custom state class for tracking messages and conversation summaries.

    Attributes:
        summary (str): A running summary of the conversation.
    """
    summary: str = ""

    def __init__(self, **kwargs):
        """
        Initialize the NewsState with optional parameters.
        
        Args:
            kwargs (dict): Initial state values.
        """
        super().__init__(**kwargs)

    def update_summary(self, new_summary: str):
        """
        Update the running summary with new content.

        Args:
            new_summary (str): The new summary to add.
        """
        self.summary = new_summary

    def reset_summary(self):
        """
        Reset the summary to an empty string.
        """
        self.summary = ""
