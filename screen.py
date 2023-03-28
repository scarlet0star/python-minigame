from battle import Battle
from character import Character
from main import create_card_instance, enemies

# 만약 여유가 있다면 텍스트는 따로 저장할 예정입니다.

start = '''김성광의 게임에 오신것을 환영합니다.\n캐릭터를 생성하거나 기존에 생성한 캐릭터를 통해 몬스터와 전투를 할 수 있습니다.'''

start_select = ["[ 캐릭터 생성하기 ]",
                "[ 캐릭터 불러오기 ]",
                "[ 게임 종료하기 ]"]

character_gen = "생성하고 싶은 캐릭터의 이름을 정해주세요."

load = "기존에 생성한 캐릭터를 불러오고 있습니다."

main = "메인 화면입니다. 하고 싶은 활동을 선택해주세요"

main_select = ["[ 장비 확인하기 ]",
               "[ 캐릭터 확인하기 ]",
               "[ 콜로세움으로 진입 ]",
               "[ 게임 종료하기 ]",]

battle = "콜로세움에 오신 것을 환영합니다. 상대할 적을 골라주세요."

battle_select = ["[ 고통스러워 하는 개발자 ]",
                 "[ 비슷한 상대 ]"]


# 스테이지 넘버를 받아 특정 스테이지의 텍스트를 출력합니다.
# return으로 해당 stage의 선택지 텍스트를 리턴합니다.

def screen_output(stage_num):
    stage_text = stage[stage_num]
    print(stage_text["text"] if stage_text["text"] != None else "")

    return stage_text["select"]

# 리턴된 선택지 리스트를 받아와서 하나씩 출력합니다.유저의 input을 리턴받습니다. 
# 이때 리스트 혹은 문자열 판별을 isinstance를 이용합니다. 이후 출력을 따로 받습니다.

def get_user_input(select):
    if isinstance(select, list):
        for i, choice in enumerate(select):
            print(f"{i + 1} | {choice}")
        user_input = int(input("\n원하는 선택지는? >> "))

    elif isinstance(select, str) and select == "input":
        user_input = input("\n값을 기입해주세요 >> ")

    else:
        user_input = ""

    return user_input

# 시작 스테이지의 선택지 로직입니다. 선택지 로직은 보통 스테이지 넘버를 리턴합니다.

def start_stage(choice, mainState):
    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    elif choice == 3:
        exit()
    else:
        print("선택지에 없는 입력을 하셨습니다. 다시 선택해주세요.")


def gen_stage(choice, mainState):
    mainState.user.name = choice

    print(f"\n환영합니다 {choice}!")
    print("캐릭터를 성공적으로 생성했습니다. 이제 게임으로 진입합니다.\n")
    return 3


def load_stage(choice, mainState):
    # json 형태로 저장할 세이브 파일을 불러오는 코드입니다. 예정사항
    print("미구현 입니다.")
    return 3


def main_stage(choice, mainState):
    if choice == 1:
        return 5
    elif choice == 2:
        return 4
    elif choice == 3:
        return 6
    elif choice == 4:
        exit()
    else:
        print("잘못된 값을 입력하셨습니다.\n")


def character_info(choice, mainState):
    print(mainState.user)
    return 3


def equip_info(choice, mainState):
    print(mainState.user.equip)
    return 3

# main.py에서 적을 생성하기 힘들어서 stage.py에서 선택지에 따라 적도 생성합니다
# 적을 생성한 이후 전투로 넘어갑니다. battle이 끝나면 다시 메인 선택지(3)으로 넘어갑니다.

def battle_stage(choice, mainState):
    enemy = Character(card_instances=create_card_instance(
        False), **enemies[str(choice)])

    battle = Battle(mainState.user, enemy)
    battle.battle(mainState.user, enemy)
    return 3

# 스테이지 정보를 담고있는 딕셔너리입니다. logic에 함수를 담아 main.py에서 불러올 수 있습니다.
# python에서는 함수 역시 1급 객체이기에 가능한 일입니다. 

stage = {
    0: {"text": start,
        "select": start_select,
        "logic": start_stage},
    1: {"text": character_gen,
        "select": "input",
        "logic": gen_stage},
    2: {"text": load,
        "select": None,
        "logic": load_stage},
    3: {"text": main,
        "select": main_select,
        "logic": main_stage
        },
    4: {"text": None,
        "select": "",
        "logic": character_info
        },
    5: {"text": None,
        "select": "",
        "logic": equip_info
        },
    6: {"text": battle,
        "select": battle_select,
        "logic": battle_stage
        }
}
