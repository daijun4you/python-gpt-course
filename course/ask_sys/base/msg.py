class Msg:
    def __init__(self) -> None:
        self.msgs = []

    def set_sys_msg(self, msg: str):
        self.msgs.insert(0, {
            "role": "system",
            "content": msg
        })

    def replace_sys_msg(self, msg: str):
        self.msgs.pop(0)
        self.set_sys_msg(msg)

    def add_user_msg(self, msg: str):
        self.msgs.append({
            "role": "user",
            "content": msg
        })

    def add_gpt_reponse(self, msg):
        self.msgs.append({
            "role": "assistant",
            "content": msg
        })

    def encode(self):
        return self.msgs
