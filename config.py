import os
from pydantic import BaseModel, Field
from typing import Optional

class Config(BaseModel):
    database_url: Optional[str] = Field(default=None, description="Optional database URL for persistent storage")
    asknews_client_id: str = Field(..., description="AskNews API Client ID")
    asknews_client_secret: str = Field(..., description="AskNews API Client Secret")
    openai_api_key: str = Field(..., description="OpenAI API Key")

def load_config() -> Config:
    # Check if required environment variables are set
    asknews_client_id = os.getenv("ASKNEWS_CLIENT_ID")
    asknews_client_secret = os.getenv("ASKNEWS_CLIENT_SECRET")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not all([asknews_client_id, asknews_client_secret, openai_api_key]):
        raise ValueError(
            "Missing required environment variables. Please ensure ASKNEWS_CLIENT_ID, "
            "ASKNEWS_CLIENT_SECRET, and OPENAI_API_KEY are set in your .env file."
        )
    
    return Config(
        database_url=os.getenv("DATABASE_URL"),
        asknews_client_id=asknews_client_id,
        asknews_client_secret=asknews_client_secret,
        openai_api_key=openai_api_key
    )
