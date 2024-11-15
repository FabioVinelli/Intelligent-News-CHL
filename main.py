from dotenv import load_dotenv
import os
from config import load_config
import sys
from agents.asknews_agent import AskNewsAgent
from agents.summarization_agent import SummarizationAgent
from agents.personalization_agent import PersonalizationAgent, UserPreferences
from agents.cross_referencing_agent import CrossReferencingAgent
from tts.tts_agent import TTSAgent

# Load environment variables from the specified .env file
env_path = os.path.join(os.path.dirname(__file__), '../.env')
if not os.path.exists(env_path):
    print(f"Error: .env file not found at {env_path}")
    sys.exit(1)

load_dotenv(env_path)

try:
    # Initialize Config
    config = load_config()
    
    # Debug: Print loaded configuration
    print("Configuration loaded successfully:")
    print(f"Database URL: {config.database_url}")
    print(f"AskNews Client ID: {'*' * 8}{config.asknews_client_id[-4:]}")
    print(f"AskNews Client Secret: {'*' * 8}{config.asknews_client_secret[-4:]}")
    print(f"OpenAI API Key: {'*' * 8}{config.openai_api_key[-4:]}")

    # Initialize agents
    asknews = AskNewsAgent(
        client_id=config.asknews_client_id,
        client_secret=config.asknews_client_secret
    )
    
    # Test news fetching
    query = "Latest developments in AI technology"
    news_articles = asknews.fetch_news(query)
    
    if news_articles:
        print(f"\nFetched {len(news_articles)} articles about '{query}'")
        for i, article in enumerate(news_articles, 1):
            print(f"\nArticle {i}:")
            print(article[:200] + "..." if len(article) > 200 else article)
    else:
        print("No articles found.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
