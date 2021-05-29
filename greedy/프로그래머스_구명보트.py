def solution(people, limit):
    people.sort(reverse=True)
    print(people)
    start, end = 0, len(people) -1
    answer = len(people)
    while start < end :
        if people[start] + people[end] <= limit :
            end -= 1
            answer -= 1
        start += 1
    return answer
