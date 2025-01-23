from mathtool import add_tool, subtract_tool, multiply_tool, divide_tool,reverse_tool,sum_of_digits_tool
from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")
#
# Initialize the OpenAI LLM
llm = OpenAI(api_key=api_key, model="gpt-3.5-turbo")

# Initialize the OpenAI Agent with tools
agent = ReActAgent.from_tools([add_tool,subtract_tool,multiply_tool,divide_tool,reverse_tool,sum_of_digits_tool], llm=llm, verbose=True)

# Interactive prompt loop
print("OpenAIAgent is ready. Type your prompt or 'q' to quit.")
while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    try:
        response = agent.chat(prompt)
        print("Response:", response)
    except Exception as e:
        print(f"An error occurred: {e}")
