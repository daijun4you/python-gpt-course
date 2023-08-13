import openai
import json
from . import plugin_networking
from configs import conf


def run():
    openai.api_key = conf.get("api_key")

    messages = [
        {"role": "user", "content": "帮我阅读一下：https://github.com/Significant-Gravitas/Auto-GPT，并给我简要介绍下"}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=messages,
    )

    return


def segAnalysis(segText: str):
    messages = [
        {"role": "user", "content": "总结这个段落的要点，要有一定的核心细节，字数控制在XX内```" + segText+"```"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=messages,
    )
