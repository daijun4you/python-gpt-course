class Plugin:
    def get_param_struct(self) -> dict:
        pass

    def get_ability(self) -> str:
        pass

    def run(self, param: dict):
        pass


# class Math(Plugin):
#     def get_param_struct(self) -> dict:
#         return {
#             "cal": "<数学公式>",
#         }

#     def get_ability(self) -> str:
#         return "数学计算"

#     def run(self, param: dict):
#         return exec(param["cal"])
