from langchain.llms import OpenAI
from configs import conf

llm = OpenAI(
    openai_api_key=conf.get("api_key"),
    temperature=0.2,
)

