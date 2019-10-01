# 두 문자열을 앞뒤로 붙여보았을 때, 더 큰 숫자에 대응되도록 문자열을 정렬한다.
# ex. '5' vs '9' : 59 < 95
# ex. '3' vs '30' : 330 > 303

# 길이가 2 이상인 문자열과 비교할 경우, (ex. 3 vs 30) 
# 문자열을 3배로 늘려보면 쉽게 비교할 수 있다. (numbers의 원소는 0 이상 1,000 이하이므로)
# 이 때, 문자열 비교 순서는 좌-> 우 !!
# '333' > '303030' 

def solution(numbers):    
    answer=''
    numbers = list(map(str, numbers))  # 정수 리스트를 문자열 리스트로 변환
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    answer = answer.join(numbers)
    
    # 주의
    if int(answer) == 0 and len(answer) > 1 :
        answer = '0'
        
    return answer