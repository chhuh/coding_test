function F(x):
    if F(x)의 문제가 간단 then :
        return F(x)를 직접 계산한 값
    딘ㄷ:
        x를 y1과 y2로 분할
        F(y1)과 F(y2)를 호출
        return F(y1), F(y2)로부터 F(x)를 구한 값
