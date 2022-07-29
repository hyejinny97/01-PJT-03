# SWEA-D2문제.신용카드 만들기 2



# 입력
'''
1. 테스트케이스 T
2. 카드번호
<카드번호로 사용가능한 조건>
- 조건1) 3, 4, 5, 6, 9로 시작
- 조건2) 자연수16개 또는 자연수16개와 '-'가 섞인 형태
'''



# 출력
'''
1. #{테스트케이스 번호} {주어진 번호로 카드번호를 만들 수 있는지}
- 만들 수 있으면, 1 출력
- 만들 수 없으면, 0 출력
'''



# 코드
import sys

sys.stdin = open("input_text/_신용카드만들기2.txt")

T = int(input())

for test_case in range(1, T + 1):
    card = input()
    # 사용가능한 카드 번호는
    # 조건1) 3, 4, 5, 6, 9로 시작
    start = '34569'
    if card[0] in start:
        # 조건2) '-'을 제외한 숫자 갯수는 16개
        cnt = 0   # 숫자 갯수
        for n in card:  
            if n != '-':
                cnt += 1
        if cnt == 16:
            print(f'#{test_case} 1')
        else:
            print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 0')