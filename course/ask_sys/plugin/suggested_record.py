from ask_sys.base import plugin


class SuggestedRecord(plugin.Plugin):
    def get_param_struct(self) -> dict:
        return {
            "suggested": "<用户建议>",
        }

    def get_ability(self) -> str:
        return "记录用户建议"

    def run(self, param: dict):
        # 这里简单演示，实际场景中，可以替换成将用户建议存储到业务数据库中
        return True
