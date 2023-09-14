import openai
from sklearn.metrics.pairwise import cosine_similarity


def run():
    # 记得改成你的api key
    openai.api_key = "sk-xxxxx"

    good_text = "这是一条好评"
    bad_text = "这是一条差评"
    evaluate_one_text = "这家餐厅太好吃了，一点都不糟糕"
    evaluate_two_text = "这家餐厅太糟糕了，一点都不好吃"

    embeddings = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=[good_text, bad_text, evaluate_one_text, evaluate_two_text],
    )

    good = embeddings["data"][0]["embedding"]
    bad = embeddings["data"][1]["embedding"]

    evaluate_one = embeddings["data"][2]["embedding"]
    evaluate_two = embeddings["data"][3]["embedding"]

    print(evaluate_one_text + ":")
    if cosine_similarity([good], [evaluate_one]) > cosine_similarity([bad], [evaluate_one]):
        print("这是一条好评")
    else:
        print("这是一条差评")

    print(evaluate_two_text + ":")
    if cosine_similarity([good], [evaluate_two]) > cosine_similarity([bad], [evaluate_two]):
        print("这是一条好评")
    else:
        print("这是一条差评")


if __name__ == "__main__":
    run()
