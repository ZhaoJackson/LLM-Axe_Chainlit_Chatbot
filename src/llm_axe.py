from src.commonconst import *

# Function to run the LLM-Axe search with more robust error handling and internet access
def search_with_llm_axe(query):
    try:
        if not query:
            raise ValueError("Query is empty or invalid")

        # Initialize the OnlineAgent for internet access
        llm = OllamaChat(model=LLAMA3_MODEL_NAME)
        searcher = OnlineAgent(llm)

        # Format the search prompt with the user query
        search_prompt = LLM_AXE_SEARCH_PROMPT.format(query=query)
        latest_info = searcher.search(search_prompt)

        if not latest_info or "Error" in latest_info:
            # Use function calling fallback to generate simple insights if the search fails
            fallback_agent = FunctionCaller(llm, [get_default_insights])
            latest_info = fallback_agent.get_function(f"Give me general insights about {query}")

        return latest_info

    except Exception as e:
        return f"Error fetching most recent info from LLM-Axe: {e}"