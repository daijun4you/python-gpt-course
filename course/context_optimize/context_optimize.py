cleanUpDataMoreThan = 1024 * 4


def cleanUpOlderContext(contextMessages):
    totalDataSize = 0
    for i, msg in enumerate(reversed(contextMessages)):
        totalDataSize += len(msg["content"])
        if totalDataSize >= cleanUpDataMoreThan:
            return contextMessages[i:]
