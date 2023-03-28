from equip import Equip

# 캐릭터 클래스입니다.
# 초기 카드 정보를 초기화할때 json의 초기 카드 id 리스트를 받아와 equip 내의 card 리스트를 구성합니다.
# __str__을 통해 캐릭터의 정보를 출력할 수 있습니다.

class Character():

    def __init__(self, card_instances, **kwargs):
        self._max_hp = kwargs.get("max_hp", 30)
        self._hp = kwargs.get("hp", 30)
        self._action = kwargs.get("action", 3)

        self._speed = kwargs.get("speed", 1)
        self._power = kwargs.get("power", 5)
        self._name = kwargs.get("name", "NONE")
        self._equip = Equip()

        card_ids = kwargs.get("cards", [])
        for card_id in card_ids:
            self._equip.add_card(card_instances[str(card_id)])

    def __str__(self):
        status = f"캐릭터 이름: {self.name}\n"
        status += f"최대 HP: {self.max_hp}\n"
        status += f"현재 HP: {self.hp}\n"
        status += f"액션 포인트: {self.action}\n"
        status += f"스피드: {self.speed}\n"
        status += f"파워: {self.power}\n"
        return status

    @property
    def max_hp(self):
        return self._max_hp

    @max_hp.setter
    def max_hp(self, value):
        if value < 0:
            self._max_hp = 1
        else:
            self._max_hp = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        elif value > self.max_hp:
            self._hp = self.max_hp
        else:
            self._hp = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def equip(self):
        return self._equip
