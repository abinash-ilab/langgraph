from llama_index.core.agent import ReActAgent
from llama_index.llms.gemini import Gemini
from mathtool import add_tool, subtract_tool, multiply_tool, divide_tool,reverse_tool,sum_of_digits_tool
import os
from dotenv import load_dotenv
load_dotenv()

llm = Gemini(
    model="models/gemini-2.0-flash-exp",
    api_key=os.getenv('GEMINI_API_KEY')
)
#agent calling 
agent = ReActAgent.from_tools([add_tool,subtract_tool,multiply_tool,divide_tool,reverse_tool,sum_of_digits_tool], llm=llm, verbose=True)

while(prompt := input("Enter a prompt (q to quit): ")) != 'q':
    response = agent.chat(prompt)
    print(response)
