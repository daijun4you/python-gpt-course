from configs import conf
import openai


def run():
    openai.api_key = conf.get("api_key")

    completion = openai.Completion.create(
        # 选择的GPT模型
        model="text-davinci-003",
        # 限制上下文最大的Token数量
        max_tokens=4000,
        # 上下文
        prompt="请介绍下自己",
        # 在GPT答复信息中需要插入的信息
        suffix="菠菜GPT技术课程",
        # 0.2使得GPT答复更具稳定性
        temperature=0.2,
        # 不采用流式输出
        stream=False,
        # 期望GPT每次答复两条（这里只是为了演示，正常情况取值为1）
        n=1,
    )

    print(completion.choices[0].text)
