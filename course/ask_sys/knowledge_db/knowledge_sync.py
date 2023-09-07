import knowledge_db


# 数据同步，实际业务场景中，可以启动定时器等定时去业务数据库中同步数据
class KnowledgeSync:
    def __init__(self) -> None:
        pass

    def sync(self):
        # 在实际场景中，可以从业务数据库获取想要建立embedding的数据进行存储
        db = knowledge_db.KnowledgeDB()
        db.add([{
            "id": "1",
            "text": "公司企业文化：做事导向、结果导向、积极补位、做事靠谱"
        }, {
            "id": "2",
            "text": "出勤要求：早9点上班，晚6点下班，不得加班"
        }, {
            "id": "3",
            "text": "发薪日：月底最后一个工作日"
        }])
