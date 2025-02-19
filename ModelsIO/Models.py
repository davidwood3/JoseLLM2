# %%
# Works with Langchain v0.3.14

"""
Models.py

This module contains the implementation of the ChatOpenAI model from LangChain,
which is used for interacting with OpenAI's GPT-3.5-turbo model.

Key Components:
- ChatOpenAI: A class for interacting with OpenAI's chat models.
- HumanMessage, SystemMessage, AIMessage: Schema classes for different types of chat messages.
"""


from langchain_openai import OpenAI
import os

OPENAI_API_KEY = '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'
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# openai.api_key = os.environ["OPENAI_API_KEY"]
print(os.environ["OPENAI_API_KEY"])


# %%
from langchain.chat_models import ChatOpenAI
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
from langchain.schema import HumanMessage, SystemMessage, AIMessage

result = chat(
    [SystemMessage(content="You are a lazy teenager who just wants to party"),
    HumanMessage(content="Tell me a fun fact about Pluto?")])
print(result.content)

# %%
from langchain.chat_models import ChatOpenAI
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
from langchain.schema import HumanMessage, SystemMessage, AIMessage

messages = [HumanMessage(content="Write a 4-line poem about a flower")]
result = chat(messages)
print(result.content)
