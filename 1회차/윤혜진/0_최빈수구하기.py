# SWEA-D2문제.최빈수 구하기



# 입력
'''
1. 테스트케이스 T
2. 테스트케이스 번호
3. 1,000명의 점수
- 0 <= 점수 <= 100
'''



# 출력
'''
1. #{테스트케이스 번호} {최빈수}
- 최빈수가 2개 이상이면 가장 큰 점수값을 출력
'''



# 코드
import sys

sys.stdin = open("input_text/_최빈수구하기.txt")

T = int(input())

for _ in range(1, T + 1):
    test_case = int(input())
    scores = map(int, input().split())   # 1000명 학생의 점수를 받음
    cnt = [0] * 101   # 인덱스: 0~100점까지의 점수, 값: 갯수

    # 1000개의 각 점수 카운트
    for score in scores:
        cnt[score] += 1
    
    # 최빈수 구하기
    max_cnt = 0   # 가장 많이 나온 점수의 갯수
    most_common_score = 0   # 가장 많이 나온 점수
    for i in range(len(cnt)):
        if cnt[i] >= max_cnt:
            max_cnt = cnt[i]
            most_common_score = i   # 더 높은 점수로 초기화 

    print(f'#{test_case} {most_common_score}')