# SWEA-D2문제.신용카드 만들기 1



# 입력
'''
1. 테스트케이스 T
2. 카드번호 자연수 15개
- 카드번호는 륜 공식을 만족해야 함

<륜 공식>
- 카드 번호에서 마지막 16번째 자리의 숫자 N을 구하는 공식
- 공식1) 매 홀수자리의 숫자마다 2를 곱해서 더함
- 공식2) 매 짝수자리의 숫자는 그대로 더함
- 공식3) 공식 1, 2에서 더한 숫자에 N을 더한 후 10으로 나누어 떨어지면 유효한 숫자
'''



# 출력
'''
1. #{테스트케이스 번호} {16번째 자리에 와야하는 수}
'''



# 코드
import sys

sys.stdin = open("input_text/_신용카드만들기1.txt")

T = int(input())
for test_case in range(1, T + 1):
    nums = [0] + list(map(int, input().split()))   # 15자리 카드 번호
    
    # 특정 조건에 따라 15자리 카드 번호 더하기
    sum_15 = 0   # 15자리 카드 번호 더한 값
    for i in range(1, 15 + 1):
        # 홀수인 경우
        if i % 2 == 1:
            sum_15 += nums[i] * 2
            continue
        # 짝수인 경우
        sum_15 += nums[i]
    
    # 16번째자리 번호 유추하기
    # (15자리 더한값 + 16째자리 번호)는 10으로 나누어 떨어져야함
    remainder = sum_15 % 10
    if remainder:   # 나누어떨어지지 않은 경우
        print(f'#{test_case} {10 - sum_15 % 10}')
    else:   # 나누어떨어진 경우
        print(f'#{test_case} 0')
        