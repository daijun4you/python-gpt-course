from ask_sys.base import plugin


class OrderSearch(plugin.Plugin):
    def get_param_struct(self) -> dict:
        return {
            "order_id": "<订单ID>",
        }

    def get_ability(self) -> str:
        return "查询订单信息"

    def run(self, param: dict):
        # 这里简单演示，实际场景中，可以替换成从业务数据库中获取
        return "订单信息：进口优质猫粮"
