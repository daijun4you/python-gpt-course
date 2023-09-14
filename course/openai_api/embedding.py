import openai


def run():
   # 记得改成你的api key
    openai.api_key = "sk-xxxxx"

    embedding = openai.Embedding.create(
        model="text-embedding-ada-002",
        input="今天天气如何",
    )

    print(embedding['data'][0]['embedding'])


if __name__ == "__main__":
    run()
