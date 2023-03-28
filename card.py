class Card:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", 0)
        self.name = kwargs.get("name", "기본 공격")
        self.action = kwargs.get("action", 1)
        self.minV = kwargs.get("minV", 1)
        self.maxV = kwargs.get("maxV", 2)
        self.effect = kwargs.get("effect", None)

    def card_effect(self, *args, **kwargs):
        if self.effect:
            self.effect(*args, **kwargs)

    def __str__(self):
        status = f"{self.name} / "
        status += f"{self.action} / "
        status += f"{self.minV}~{self.maxV} / "
        status += f"{self.effect}"
        return status
