Set : 수학에서의 집합과 비슷하다.
주요 특징
- 순서가 없고 집합안에서는 unique한 값을 가진다.
- 중괄호를 사용하지만, dictionary와는 다르게 key가 없고, value만 존재한다.
- mutable한 값을 value로 지닐 수 없다.(ex. list)

1. 생성
    - s = {3,5,7}   
    - s = set()
    - s = set([3,5,7])   * iterable한 객체를 넣으면 변환하여 set으로 만들어 준다.
    
2. 추가
    # 1개씩 추가
    - s.add(50)
    # 여러개 추가
    - s.update([3,5,7])
    
3. 제거
    # s내의 원소를 제거하고 만약 제거하고자 하는 원소가 s내에 없는 경우 error발생
    - s.remove(5)
    # s내의 원소를 제거하고 제거하고자 하는 원소가 s내에 존재하지 않아도 error 발생하지 않음
    - s.discard(22)
    
4. 집합 연산 method
    >>> a = {1, 2, 3, 4, 5}
    >>> b = {3, 4, 5, 6, 7}    
    - union(합집합)
        >>> c = a.union(b)
        >>> c
        {1, 2, 3, 4, 5, 6, 7}
    
    - intersection(교집합)
        >>> c = a.intersection(b)
        >>> c
        {3, 4, 5}
        
    - difference(차집합)
        >>> c = a.difference(b)
        >>> c
        {1, 2}
        
    - symmetric_difference(합집합 - 교집합)
        >>> c = a.symmetric_difference(b)
        >>> c
        {1, 2, 6, 7}
    
5. 관련 함수들
    >>> a = {1, 2, 3, 4, 5}
    >>> b = {1, 2, 3}
    - issubset() : subset(부분집합)인지 확인
        >>> a.issubset(b)
        False
        >>> b.issubset(a)
        True
    
    - issuperset() : superset인지 확인
        >>> a.issuperset(b)
        True
        >>> b.issuperset(a)
        False
        
    - isdisjoint() : 교집합이 없으면 True, 있으면 False
        >>> a = {1, 2, 3}
        >>> b = {4, 5, 6}
        >>> a.isdisjoint(b)
        True
        >>> c = {1, 2, 3}
        >>> d = {3, 4, 5}
        >>> c.isdisjoint(d)
        False
