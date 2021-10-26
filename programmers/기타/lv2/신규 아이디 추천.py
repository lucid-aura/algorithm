import re
def solution(new_id):
    print(0, new_id)
    # 1단계 대문자 -> 소문자
    new_id = new_id.lower()
    print(1, new_id)
    # 2단계 !@#* 제거
    new_id = re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:?,\<\>/]','',new_id)
    # new_id = new_id.replace('!', '')
    # new_id = new_id.replace('@', '')
    # new_id = new_id.replace('#', '')
    # new_id = new_id.replace('*', '')
    print(2, new_id)
    # 3단계  .이 복수개이면 . 하나로
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    print(3, new_id)
    # 4단계 마침표 처음과 끝 제거
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    print(4, new_id)
    # 5단계 빈문자열이면 a로 대체
    if len(new_id) == 0:
        new_id = "a"
    print(5, new_id)
    # 6단계 길이가 16자 이상이면 줄이기
    if len(new_id) > 16:
        new_id = new_id[:16]
        if new_id[15] == '.':
            new_id = new_id[:15]
    print(6, new_id)
    # 7단계 길이 3까지 마지막 문자 붙이기
    while len(new_id) < 3:
        new_id += new_id[-1]
    answer = new_id
    print(7, answer)
    
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "abcdefghijklmn.p"	
# new_id = "=.="	
solution(new_id)
