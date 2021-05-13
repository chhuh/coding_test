Dictionary : Key와 Value를 한 쌍으로 가지는 자료형이다.
1. 생성
    - dic = {}
    - dic = {1 : 'hi'}
    
2. 추가
    - >>> a = {1: 'a'}
      >>> a[2] = 'b'
      >>> a
      {1: 'a', 2: 'b'}
      
3. 삭제
    - >>> del a[1]
      >>> a
      {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

4. 주의사항
    - Key는 중복될 수 없음
      >>> a = {1:'a', 1:'b'}
      >>> a
      {1: 'b'}

    - list는 Key로 사용될 수 없음

5. 관련 함수들
    - keys() : keys()는 딕셔너리의 Key만을 모아서 dict_keys 객체를 돌려준다.
    - values() : values()는 딕셔너리의 value만을 모아서 dict_values 객체를 돌려준다.
    - items() : tems 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
    - clear() : clear 함수는 딕셔너리 안의 모든 요소를 삭제한다.
    - get() : get(x) 함수는 x라는 Key에 대응되는 Value를 돌려준다.
