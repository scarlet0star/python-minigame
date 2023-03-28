from screen import *
from card import Card
from character import Character
from utils import load_files

# json 파일을 불러옵니다. 이를 통해 json에서 데이터를 꺼내 언제든지 객체를 인스턴스화 할 수 있습니다.
cards = load_files("card_list.json")
enemies_cards = load_files("enemy_card_list.json")
heroes = load_files("hero_character.json")
enemies = load_files("enemy_character.json")


# 카드 객체를 생성시 사용하는 함수입니다. bool 값으로 player, enemy를 결정합니다.
# Character class 생성시 character.json에 존재하는 기본 스킬 id list를 이용하여 초기 카드 소지 정보를 초기화합니다.

def create_card_instance(isUser=False):
    card = cards if isUser else enemies_cards

    instance = {
        card_id: Card(
            card_id=card_info["id"],
            name=card_info["name"],
            action=card_info["action"],
            minV=card_info["minV"],
            maxV=card_info["maxV"],
            effect=card_info["effect"],
        )
        for card_id, card_info in card.items()
    }

    return instance

# main 상태입니다. 현재는 스테이지 정보와 player character에 대한 정보밖에 없습니다.


class MainState:
    def __init__(self, user):
        self.user = user
        self.stage = 0

# main입니다. While 문을 통해 stage.py에서 선택지 정보를 받아와 계속 출력합니다.
# 현재 player 캐릭터를 하나만 지정했기 때문에 **heroes['1']로 하드코딩 되어있습니다.
# 만약 player 캐릭터를 늘릴 예정이라면 추가적인 선택지를 제시하여 선택할 수 있게 할 예정입니다.


def main():
    user = Character(card_instances=create_card_instance(True), **heroes['1'])
    mainState = MainState(user)
    while True:
        text = screen_output(mainState.stage)
        select = get_user_input(text)

        next_stage = stage.get(mainState.stage).get("logic")(
            select, mainState)

        mainState.stage = next_stage


if __name__ == '__main__':
    main()
