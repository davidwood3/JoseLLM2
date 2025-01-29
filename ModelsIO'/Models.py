# %%
# Works with Langchain v0.3.14

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



