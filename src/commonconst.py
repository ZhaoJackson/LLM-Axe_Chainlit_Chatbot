from llm_axe import OnlineAgent, OllamaChat, FunctionCaller
import ollama
import chainlit as cl
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuration Constants
LLM_AXE_SEARCH_PROMPT = (
    "Please retrieve the most up-to-date and reliable information on '{query}', "
    "from general trusted websites like news portals, technology blogs, or well-known publications. "
    "Include the publication date if available."
)

LLAMA3_RESPONSE_PROMPT = (
    "Using the most recent information retrieved on '{query}', summarize key trends and insights. "
    "Here is the most up-to-date info:\n\n{latest_info}\n\n"
    "Summarize this information into a short blog post."
)

LLAMA3_FALLBACK_PROMPT = (
    "Based on the general information found on '{query}', provide a blog post summary "
    "that includes key insights and trends."
)

# External Dependencies
LLAMA3_MODEL_NAME = "llama3:instruct"
OLLAMA_CHAT_ROLE = "user"