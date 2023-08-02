import requests


# 定义访问网络的plugin
def networking(params):
    return requests.get(params.get("url")).text


# 为GPT提供networking的描述
def get_networking_desc():
    return {
        "name": "networking",
        "description": "可以通过这个函数访问网络",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "需要访问的url",
                }
            }
        },
    }
