# SWEA-D3문제.문자열의 거울상



# 입력
'''
1. 테스트케이스 T
2. 'b','d','p','q'로 이루어진 문자열
- 1 <= 문자열 길이 <= 1,000
'''



# 출력
'''
1. #{테스트케이스 번호} {거울에 비춰진 문자열}
'''



# 코드
import sys

sys.stdin = open("input_text/_문자열의거울상.txt")

T = int(input())

for test_case in range(1, T + 1):
    word = input()
    mirror = {   # 각 알파벳을 거울에 비춘 모습
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p'
    }

    # 입력받은 문자열을 거울에 비추기
    # 각 알파벳 좌우로 뒤집기 + 역순
    rst = ''
    for char in word:
        rst += mirror[char]

    print(f'#{test_case} {rst[::-1]}')