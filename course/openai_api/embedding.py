from configs import conf
import openai


def run():
    openai.api_key = conf.get("api_key")

    embedding = openai.Embedding.create(
        model="text-embedding-ada-002",
        input="今天天气如何",
    )

    print(embedding['data'][0]['embedding'])
