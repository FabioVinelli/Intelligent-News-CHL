from pydantic import BaseModel, Field
from typing import List, Optional

class NewsArticle(BaseModel):
    """
    A class to represent a news article.

    Attributes:
        id (int): The unique identifier for the article.
        title (str): The title of the article.
        summary (str): A brief summary of the article.
        content (Optional[str]): The full content of the article (if available).
        entities (Optional[List[str]]): A list of entities mentioned in the article.
        sentiment (Optional[str]): The sentiment of the article (if analyzed).
        source (str): The source of the article.
    """
    id: int
    title: str
    summary: str
    content: Optional[str] = None
    entities: Optional[List[str]] = []
    sentiment: Optional[str] = None
    source: str

class Settings(BaseModel):
    """
    A class to represent application settings.

    Attributes:
        debug (bool): Enable debug mode.
        database_url (str): Database connection URL.
        asknews_client_id (str): AskNews API Client ID.
        asknews_client_secret (str): AskNews API Client Secret.
        openai_api_key (str): OpenAI API Key.
    """
    debug: bool = Field(default=False, description="Enable debug mode")
    database_url: str = Field(..., description="Database connection URL")
    asknews_client_id: str = Field(..., description="AskNews API Client ID")
    asknews_client_secret: str = Field(..., description="AskNews API Client Secret")
    openai_api_key: str = Field(..., description="OpenAI API Key")
