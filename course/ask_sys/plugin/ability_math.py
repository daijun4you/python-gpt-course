from ask_sys.base import plugin


class Math(plugin.Plugin):
    def get_param_struct(self) -> dict:
        return {
            "cal": "<数学公式>",
        }

    def get_ability(self) -> str:
        return "数学计算"

    def run(self, param: dict):
        return exec(param["cal"])
