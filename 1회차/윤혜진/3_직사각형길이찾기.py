# SWEA-D3문제.직사각형 길이 찾기



# 입력
'''
1. 테스트케이스 T
2. 3개의 자연수 a, b, c
- 1 <= a, b, c <= 100
'''



# 출력
'''
1. #{테스트케이스 번호} {나머지 한 변의 길이}
'''



# 코드
import sys

sys.stdin = open("input_text/_직사각형길이찾기.txt")

T = int(input())

for test_case in range(1, T + 1):
    lengths = list(map(int, input().split()))   # 인덱스 0, 1, 2
    
    # 나머지 한 변(last) = 같은 길이의 변을 제외한 변
    for i in range(1, 3):
        if lengths[0] == lengths[i]:
            last = lengths[3 - i]   # 인덱스 총합 = 3
            break
    # break없이 나왔다면, 0번째 인덱스가 나머지 한 변과 동일한 길이
    else:
        last = lengths[0]

    print(f'#{test_case} {last}')