import json

# 추가적인 기능들을 위한 파일입니다. 현재는 json파일을 불러오고 리턴해주는 함수밖에 없습니다.

def load_files(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        file_data = json.load(f)
    return file_data

