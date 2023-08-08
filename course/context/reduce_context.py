# contextMessages = [
#     {"role": "system", "content": "你是一个资深的心理咨询师"},
#     {"role": "user", "content": "我觉得GPT很酷！"}
# ]

cleanUpDataMoreThan = 1024 * 4


def cleanUpOlderContext(contextMessages):
    totalDataSize = 0
    for i, msg in enumerate(reversed(contextMessages)):
        totalDataSize += len(msg["content"])
        if totalDataSize >= cleanUpDataMoreThan:
            return contextMessages[i:]
