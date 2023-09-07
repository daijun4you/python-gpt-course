class Plugin:
    # 获取参数结构
    def get_param_struct(self) -> dict:
        pass

    # 获取插件能力描述
    def get_ability(self) -> str:
        pass

    # 执行插件
    def run(self, param: dict):
        pass
