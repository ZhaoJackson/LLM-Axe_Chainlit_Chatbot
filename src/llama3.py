from src.commonconst import *

# Function to generate a response using Llama3
def generate_llama3_response(query, latest_info):
    try:
        # Use the appropriate prompt based on the availability of `latest_info`
        if latest_info and "Error" not in latest_info:
            response_prompt = LLAMA3_RESPONSE_PROMPT.format(query=query, latest_info=latest_info)
        else:
            response_prompt = LLAMA3_FALLBACK_PROMPT.format(query=query)

        # Generate response using Llama3 model
        blog_response = ollama.chat(model=LLAMA3_MODEL_NAME, messages=[{"role": OLLAMA_CHAT_ROLE, "content": response_prompt}])
        blog_content = blog_response['message']['content']

        return blog_content

    except Exception as e:
        return f"Error generating the response with {LLAMA3_MODEL_NAME}: {e}"