# src/agents.py

class OnlineAgent:
    def __init__(self, llm):
        self.llm = llm

    def search(self, prompt):
        # Replace with real web search logic if needed
        return f"Simulated search result for: {prompt}"

class OllamaChat:
    def __init__(self, model, base_url="http://localhost:11434"):
        self.model = model
        self.base_url = base_url

    def chat(self, prompt):
        # Replace with call to actual Ollama endpoint
        return f"Simulated Llama3 response for: {prompt}"


class FunctionCaller:
    def __init__(self, llm, functions):
        self.llm = llm
        self.functions = functions

    def get_function(self, prompt):
        return f"Fallback output for: {prompt}"