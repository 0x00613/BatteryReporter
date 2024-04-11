import re

def extractNumbers(inputString):
    # 숫자만 남기기
    result = re.sub(r'\D', '', inputString)
    return int(result)