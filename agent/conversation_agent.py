from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from chain.llm_chain import llm_chain
from tool.datetime_tool import Datetime
from model.openai import llm
memory = ConversationBufferMemory(memory_key="chat_history")
tools = [
    Datetime
]
agent_chain = initialize_agent(llm_chain=llm_chain, llm=llm, tools=tools,
                               agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True,
                               memory=memory)
