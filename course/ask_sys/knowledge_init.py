from ask_sys.knowledge_db import knowledge_sync


def run():
    # 初始化知识库
    knowledge_sync.KnowledgeSync().sync()
