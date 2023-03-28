import random
from itertools import zip_longest


class Battle:
    def __init__(self, player_character, enemy_character):
        self.battle_round = 1
        self.player_character = player_character
        self.enemy_character = enemy_character

        self.player_hand = []
        self.player_graveyard = []
        self.enemy_hand = []
        self.enemy_graveyard = []

        self.player_actions = []
        self.enemy_actions = []

        self.backup = player_character

    def draw_cards(self, character, hand, graveyard, nums=1):
        # 카드를 뽑기. 덱과 핸드, 무덤의 카드 수를 비교하여 세 리스트 사이에서 카드를 서로 옮깁니다.
        deck = character.equip.card_list
        max_val = character.equip.max
        # 카드 드로우는 한번씩 진행됩니다. 덱이 비어있다면 무덤을 비우고 덱으로 채웁니다.
        for draw_count in range(nums):
            if len(deck) - 1 < 0:
                print("덱이 비었기에 무덤의 카드를 다시 덱으로 불러옵니다\n")
                deck = graveyard[::]
                graveyard.clear()
            if len(hand) < max_val:
                draw = random.choice(deck)
                deck.remove(draw)
                hand.append(draw)
            else:
                print("핸드가 가득찼기에 카드를 뽑지 않습니다.\n")

    def enemy_place_card(self, enemy, hand, graveyard):
        action_list = []
        for speed in range(enemy.speed):
            available_card = random.choice(
                [card for card in hand if card.action <= enemy.action])
            action_list.append(available_card)
            hand.remove(available_card)
            graveyard.append(available_card)

        return action_list

    def start(self):
        # 전투 최초 시작시 일어날 일, 추후 계획에 따라 더 추가될 여지 있음
        # 플레이어와 적이 모두 카드를 3장씩 뽑습니다.
        self.draw_cards(self.player_character, self.player_hand,
                        self.player_graveyard, 3)
        self.draw_cards(self.enemy_character, self.enemy_hand,
                        self.enemy_graveyard, 3)

    def round_start(self):
        # 매 라운드 시작시 마다 일어날 로직을 작성합니다.
        # 플레이어와 적이 모두 카드를 1장씩 뽑습니다.
        self.draw_cards(self.player_character,
                        self.player_hand, self.player_graveyard)
        self.draw_cards(self.enemy_character,
                        self.enemy_hand, self.enemy_graveyard)

        self.enemy_actions = self.enemy_place_card(
            self.enemy_character, self.enemy_hand, self.enemy_graveyard)

    def player_setting(self):
        print("\n적이 아래와 같이 공격합니다. 어떻게 대응하나요?")

        temp_actions = []
        temp_graveyard = []
        temp_hand = self.player_hand[::]
        temp_action_points = self.player_character.action

        while True:

            for my_attack, ene_attack in zip_longest(temp_actions, self.enemy_actions, fillvalue="empty"):
                print(f'>>>>> {my_attack} vs {ene_attack} <<<<<')

            print("\n현재 패에 아래와 같은 카드가 있습니다")
            print("카드명 / 액션소모 / 카드 값 / 특수 효과")
            for idx, card in enumerate(self.player_hand, start=1):
                print(f'{idx} : {card}')

            player_choice = int(input(
                f"대응할 카드 번호를 입력해주세요 : 현재 배치 가능 갯수 / 액션 포인트 : ({self.player_character.speed} / {self.player_character.action}) "))

            if 1 <= player_choice <= len(temp_hand):
                selected_card = temp_hand[player_choice - 1]
                if temp_action_points >= selected_card.action:
                    temp_actions.append(selected_card)

                    temp_hand.remove(selected_card)
                    temp_graveyard.append(selected_card)
                    temp_action_points -= selected_card.action
                else:
                    print("액션 포인트가 부족합니다.\n")
            else:
                print("잘못된 입력입니다.\n")

            if self.player_character.speed == len(temp_actions) or temp_action_points <= 0:
                print(
                    f"\n액션 포인트 소모량 : {self.player_character.action - temp_action_points}")
                for my_attack, ene_attack in zip_longest(temp_actions, self.enemy_actions, fillvalue="empty"):
                    print(f'>>>>> {my_attack} vs {ene_attack} <<<<<')

                confirm = input("\n선택한 카드로 진행하시겠습니까? (1: 예, 0: 아니오) ")

                if confirm == "1":
                    self.player_actions = temp_actions
                    self.player_graveyard = temp_graveyard
                    self.player_hand = temp_hand
                    self.player_character.action = temp_action_points
                    break
                elif confirm == "0":
                    temp_actions = []
                    temp_graveyard = []
                    temp_hand = self.player_hand[::]
                    temp_action_points = self.player_character.action

    def after_setting(self):
        for player_card, enemy_card in zip(self.player_actions, self.enemy_actions):
            player_damage = self.player_character.power + \
                random.randint(player_card.minV, player_card.maxV)
            enemy_damage = self.enemy_character.power + \
                random.randint(enemy_card.minV, enemy_card.maxV)

        print(f"\n플레이어 스킬의 위력 : {player_damage} vs 적 스킬의 위력 {enemy_damage}!!")
        if player_damage > enemy_damage:
            self.enemy_character.hp -= player_damage
            print(
                f"{self.player_character.name}이(가) {self.enemy_character.name}에게 {player_damage}의 데미지를 입혔습니다.")
        elif enemy_damage > player_damage:
            self.player_character.hp -= enemy_damage
            print(
                f"{self.enemy_character.name}이(가) {self.player_character.name}에게 {enemy_damage}의 데미지를 입혔습니다.")
        else:
            print("두 캐릭터의 데미지가 동일하여 아무런 피해도 입히지 못했습니다.")

    def battle(self, player, enemy):

        self.start()

        while player.hp > 0 and enemy.hp > 0:
            player_status = str(player).split('\n')
            enemy_status = str(enemy).split('\n')

            print(f'{self.battle_round}라운드가 시작되었습니다\n')
            print("플레이어 상태 vs 적 상태")
            for p_line, e_line in zip(player_status, enemy_status):
                print(f"{p_line:<25} {e_line}")

            self.round_start()
            self.player_setting()
            self.after_setting()
            print("라운드 종료! 액션 포인트가 2씩 증가합니다.\n")
            self.player_character.action += 2
            self.enemy_character.action += 2
            self.battle_round += 1

            if self.player_character.hp <= 0:
                print("\n패배 했습니다...\n")
            elif self.enemy_character.hp <= 0:
                print("\n승리!\n")

        self.player_character = self.backup

        return 3
