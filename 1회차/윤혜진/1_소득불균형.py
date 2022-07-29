# SWEA-D3문제.소득 불균형



# 입력
'''
1. 테스트케이스 T
2. 소득 갯수 N
- 1 <= N <= 10,000
3. 각 사람의 소득 N개
- 1 <= 소득 <= 100,000
'''



# 출력
'''
1. #{테스트케이스 번호} {평균 소득 이하의 소득을 가진 사람의 수}
'''



# 코드
import sys

sys.stdin = open("input_text/_소득불균형.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())   # 사람 수
    incomes = list(map(int, input().split()))   # 각 사람의 수입

    # 평균 소득 구하기
    avg = sum(incomes) / N

    # 평균 소득 이하의 소득을 가지는 사람 수 구하기
    cnt = 0
    for income in incomes:
        if income <= avg:
            cnt += 1
    
    print(f'#{test_case} {cnt}')