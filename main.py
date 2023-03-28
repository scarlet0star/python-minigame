from screen import *
from equip import Equip
from card import Card
from character import Character
from utils import load_files

cards = load_files("card_list.json")
enemies_cards = load_files("enemy_card_list.json")
heroes = load_files("hero_character.json")
enemies = load_files("enemy_character.json")


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


class MainState:
    def __init__(self, user):
        self.user = user
        self.stage = 0


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
