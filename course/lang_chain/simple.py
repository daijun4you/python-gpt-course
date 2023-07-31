from langchain import PromptTemplate, OpenAI, LLMChain
from configs import conf


def run():
    llmOpenAI = OpenAI(
        temperature=0.2,
        openai_api_key=conf.get("api_key")
    )

    for i in dir(PromptTemplate):
        print(i)

    prompt = PromptTemplate.from_template("将用户输入的信息以JSON格式进行返回")

    # llmChain = LLMChain(
    #     llm=llmOpenAI,
    #     prompt=prompt,
    # )

    # resp = llmChain.apply(
    #     [
    #         "今天天气不错",
    #         "北京的天气太热了",
    #         "上海天气适中"
    #     ]
    # )

    # for one in range(resp):
    #     print(one)
