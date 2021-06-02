def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    # x*3으로 충분한 이유 주어진 숫자가 0이상 1000이하이기 때문에
    answer = str(int(''.join(numbers)))
    # int로 변환했다가 다시 str로 변환하는 이유 : 0만 있는 경우 생각
    return answer
