from src.commonconst import *
from src.llm_axe import search_with_llm_axe
from src.llama3 import generate_llama3_response

# Chainlit handler for chat interaction
@cl.on_message
async def on_message(message):
    query = message.content

    # Inform the user that the query is being processed
    await cl.Message(content=f"Searching for the most recent and up-to-date info on: {query}").send()

    # Fetch the most recent info using LLM-Axe
    latest_info = search_with_llm_axe(query)

    if "Error" in latest_info:
        # Inform the user if LLM-Axe couldn't find specific information
        await cl.Message(content=f"No specific recent information was found for '{query}', generating a general summary.").send()
    
    # Generate a response using Llama3 based on the retrieved info
    final_response = generate_llama3_response(query, latest_info)

    # Display both the latest info and Llama3's final response
    await cl.Message(content=f"Most Recent Info on {query}:\n{latest_info}").send()
    await cl.Message(content=f"{LLAMA3_MODEL_NAME} Response:\n{final_response}").send()