from langchain.llms import OpenAI
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from configs import conf


def run():
    # 加载将要用来控制 Agents 的语言模型
    llm = OpenAI(temperature=0.2, openai_api_key=conf.get("api_key"))

    # 加载一些要使用的工具
    tools = load_tools(["serpapi", "llm-math"], llm=llm)

    # 初始化 Agents
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    # 测试一下！
    agent.run("姚明的妻子是谁？她现在的年龄是多少？她年龄的0.76次方是多少？")
