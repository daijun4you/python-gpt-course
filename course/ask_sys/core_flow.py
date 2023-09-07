from ask_sys.base import prompt
from ask_sys.plugin import ability_math, order_search, suggested_record
from ask_sys.knowledge_db import knowledge_db
import json
import openai
from configs import conf

openai.api_key = conf.get("api_key")


def run():
    # ----------------- 初始化 -----------------
    sysPrompt = prompt.SysPrompt()
    init_plugin(sysPrompt)
    kdb = knowledge_db.KnowledgeDB()

    print(sysPrompt.encode())

    # 将SysPrompt放入msg中
    msgs = [
        {"role": "system", "content": sysPrompt.encode()},
    ]

    # 模拟用户输入，实际场景中，往往会从Http请求中获取
    user_prompt = mock_user_prompt_ask_company_culture()
    # 查询知识库
    result = kdb.search(user_prompt)
    knowledge = ""
    # 如果知识库查出内容，可将内容放入上下文
    if len(result["documents"]) > 0:
        knowledge = json.dumps(result["documents"])

    # 用户prompt加入上下文
    msgs.append({"role": "user", "content": sysPrompt.build_user_prompt(
        user_prompt=user_prompt, knowledge=knowledge)})

    print(msgs)

    # 与GPT交互
    chat_completion = openai.ChatCompletion.create(
        # 选择的GPT模型
        model="gpt-3.5-turbo-16k-0613",
        # 上下文
        messages=msgs,
        # 1.2使得GPT答复更具随机性
        temperature=0.2,
        # 不采用流式输出
        stream=False,
    )

    # 系统回复加入上下文
    msgs.append(chat_completion.choices[0].message)

    print(chat_completion.choices[0].message.content)

    # 处理GPT响应
    response = json.loads(
        chat_completion.choices[0].message.content)["response"]
    # 直接输出结果
    if response["type"] == "normal":
        print(response["normal"])
    # 命中了组件
    else:
        plugin = sysPrompt.get_plugin(response["type"])
        if plugin is None:
            return

        run_result = plugin.run(response[response["type"]])
        msgs.append({
            "role": "system",
            "content": "调用插件结果：'''" + json.dumps(run_result) + "'''"
        })

        chat_completion = openai.ChatCompletion.create(
            # 选择的GPT模型
            model="gpt-3.5-turbo-16k-0613",
            # 上下文
            messages=msgs,
            # 1.2使得GPT答复更具随机性
            temperature=0.2,
            # 不采用流式输出
            stream=False,
        )

        print(chat_completion.choices[0].message.content)


def mock_user_prompt_search_order():
    return "帮我查下订单信息，订单号：123456"


def mock_user_prompt_ask_company_culture():
    return "咱公司有啥企业文化？"


# 初始化插件
def init_plugin(p: prompt.SysPrompt):
    p.add_plugin(ability_math.Math())
    p.add_plugin(order_search.OrderSearch())
    # p.add_plugin(suggested_record.SuggestedRecord())
