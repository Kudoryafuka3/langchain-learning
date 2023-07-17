from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.agents import initialize_agent

memory = ConversationBufferMemory(memory_key="chat_history")
llm = OpenAI(model="text-davinci-003", temperature=0)
tools = []
agent_chain = initialize_agent(llm=llm, tools=tools, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True,
                               memory=memory)
