def solution(n):
    answer = ''
    sample = '수박'
    if n%2 == 1:
        for _ in range(n//2):
            answer += sample
        answer += '수'
    else:
        for _ in range(n//2):
            answer += sample
    return answer
print(solution(3))