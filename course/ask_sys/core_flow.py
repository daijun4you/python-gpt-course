from ask_sys.base import prompt, msg
from ask_sys.plugin import ability_math, order_search, suggested_record
from ask_sys.knowledge_db import knowledge_db
import json
import openai
from configs import conf

sys_prompt = prompt.SysPrompt()
kdb = knowledge_db.KnowledgeDB()
msg = msg.Msg()

openai.api_key = conf.get("api_key")


def run():
    init_plugin()

    msg.set_sys_msg(sys_prompt.encode())

    # 模拟用户输入，实际场景中，往往会从Http请求中获取
    user_prompt = mock_user_prompt_search_order()
    # 查询知识库
    result = kdb.search(user_prompt)

    knowledge = ""
    # 如果知识库查出内容，可将内容放入上下文
    if len(result["documents"]) > 0:
        knowledge = json.dumps(result["documents"])

    # 用户prompt加入上下文
    msg.add_user_msg(sys_prompt.build_knowledge_prompt(
        user_prompt=user_prompt, knowledge=knowledge))

    # 与GPT交互
    gpt_msg = request_gpt()

    # 系统回复加入上下文
    msg.add_gpt_reponse(gpt_msg.content)

    # 处理GPT响应，并兼容gpt返回的不稳定性
    response = json.loads(gpt_msg.content)
    if response.get("response") is not None:
        response = response.get("response")

    if not isinstance(response, dict):
        print(response)
    elif response.get("normal") is not None:
        print(response["normal"])
    else:
        call_plugin(response, user_prompt=user_prompt)


def call_plugin(response, user_prompt):
    plugins = sys_prompt.get_plugins()
    for pluginName, plugin in plugins.items():
        if response.get(pluginName) is not None:
            run_result = plugin.run(response.get(pluginName))

            msg.set_sys_msg(sys_prompt.encode_no_plugin())
            msg.add_user_msg(sys_prompt.build_plugin_prompt(
                user_prompt=user_prompt, plugin_response=json.dumps(run_result)))

            # print(msg.encode())

            print(request_gpt().content)

            break


def request_gpt():
    chat_completion = openai.ChatCompletion.create(
        # 选择的GPT模型
        model="gpt-3.5-turbo-16k-0613",
        # 上下文
        messages=msg.encode(),
        # 1.2使得GPT答复更具随机性
        temperature=0.2,
        top_p=0.2,
        # 不采用流式输出
        stream=False,
    )

    return chat_completion.choices[0].message


def mock_user_prompt_search_order():
    return "帮我查下订单信息，订单号：123456"


def mock_user_prompt_ask_company_culture():
    return "咱公司有啥企业文化？以及上班时间呢？"


# 初始化插件
def init_plugin():
    sys_prompt.add_plugin(ability_math.Math())
    sys_prompt.add_plugin(order_search.OrderSearch())
    sys_prompt.add_plugin(suggested_record.SuggestedRecord())
