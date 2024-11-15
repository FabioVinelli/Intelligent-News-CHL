class BaseAgent:
    """
    Base class for all agents in the system.
    Provides common functionality and interface that all agents should implement.
    """
    
    def __init__(self):
        """Initialize the base agent."""
        pass

    def log(self, message: str):
        """
        Log a message with the agent's name.
        
        Args:
            message (str): The message to log.
        """
        print(f"[{self.__class__.__name__}] {message}")

    def handle_error(self, error: Exception, context: str = ""):
        """
        Handle errors in a consistent way across all agents.
        
        Args:
            error (Exception): The error that occurred
            context (str): Additional context about where/why the error occurred
        """
        error_message = f"Error in {context}: {str(error)}"
        self.log(error_message)
        return None
