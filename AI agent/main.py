from dotenv import load_dotenv
import os
from llama_index.experimental.query_engine import PandasQueryEngine
from prompt import context, new_prompt
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
from note_engine import note_engine, reading_engine
from reading_pdf import index_engine
from memery import memory
load_dotenv()
history_path = os.path.join("data", "history.txt")
session_id = 1
tool = [
    reading_engine,
    note_engine,
    QueryEngineTool(
        query_engine=index_engine,
        metadata=ToolMetadata(
            name='reading pdf', 
            description='this gives information and data of how you response to question'))
]

llm = OpenAI(model="gpt-4-turbo")
agent = ReActAgent.from_tools(tools=tool, llm=llm, contex=context)

prompt = input("How acn I help you today? (enter q to quit):")
while prompt != "q":
    prompt = memory.get_session_history(session_id) + "current prompt: " + prompt
    response = agent.query(prompt)
    print(response)
    memory.add_interaction(session_id, prompt, response)
    prompt = input("How can I help you today? (enter q to quit):")

