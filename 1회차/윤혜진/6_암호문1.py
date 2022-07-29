# SWEA-D3문제.암호문1



# 입력
'''
(테스트케이스 T = 10)
1. 원본 암호문 길이 N
- 10 <= N <= 20
2. 원본 암호문
- 0 <= 정수 <= 999,999
3. 명령어 갯수 M
- 5 <= M <= 10
4. 명령어
'''



# 출력
'''
1. #{테스트케이스 번호} {수정된 암호문의 처음 10개 항}
'''



# 코드 1
import sys

sys.stdin = open("input_text/_암호문1.txt")

T = 10
for test_case in range(1, T + 1):
    original_N = int(input())   # 원본 암호본 갯수
    original = list(map(int, input().split()))   # 원본 암호문
    doit_N = int(input())   # 명령어 갯수
    doit = [list(map(int, one.split())) for one in input().split('I ')[1:]]   # 명령어
    
    # 명령어에 따라 원본 암호문 수정
    update = original   # 수정된 암호문
    for i in range(0, doit_N):
        insert_loc = doit[i][0]   # 삽입 위치
        update = update[0:insert_loc] + doit[i][2:] + update[insert_loc:]

    print(f'#{test_case}', *update[:10])



# 코드 2 - 슬라이싱을 이용해서 삽입
sys.stdin = open("input_text/_암호문1.txt")

T = 10
for test_case in range(1, T + 1):
    original_N = int(input())   # 원본 암호본 갯수
    original = list(map(int, input().split()))   # 원본 암호문
    doit_N = int(input())   # 명령어 갯수
    doit = [list(map(int, one.split())) for one in input().split('I ')[1:]]   # 명령어
    
    # 명령어에 따라 원본 암호문 수정
    update = original   # 수정된 암호문
    for i in range(0, doit_N):
        insert_loc = doit[i][0]   # 삽입 위치
        update[insert_loc:insert_loc] = doit[i][2:]

    print(f'#{test_case}', *update[:10])