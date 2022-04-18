##
# HW NUMBER: 2
# FILE NAME : solvingCh5ProgrammingProblems.py
# AUTHOR :
#   학과 & 학년: 컴퓨터공학과 1학년
#   학번 & 이름: C211123 이준선
# YYYYMMDD : 2020.04.04 (THE DATE MUST BE HERE.)
# PURPOSE : 5 장 Programming 문제 중 4, 8, 9, 10 번 문제들을, 수업시간에 공지한대로, main() 함수 안에서
# 차례대로 호출하여 그 결과를 아래 출력결과 예시와 같이 출력하는 프로그램을 작성하시오. (각
# 함수에 대한 입력 데이터는 자유롭게 선택할 수 있음).

# COMMENTS: The following function definitions are for solving the programming problem
#                       of the chapter 5: 4,8,9, and 10.

#score를 기준으로 성적을 반환하는 함수
#score의 기준이 0~100까지라는 기준이 없으므로, score > 100 || score < 0 인 상황에 대한 예외 처리는 하지 않음
def getGrade(score):
    if score > 90:
        return 'A'
    elif score > 80:
        return 'B'
    elif score > 70:
        return 'C'
    elif score > 60:
        return 'D'
    else:
        return 'F'

#정수 money를 입력받아, 이를 한국어로 바꿔주는 함수
def getMoneyText(money):
    number_unit = {1:'일', 2:'이', 3:'삼', 4:'사', 5:'오', 6:'육',\
                 7:'칠', 8:'팔', 9:'구'} #int형 숫자를 한국어로 변환하는 딕셔너리
    money_unit = ['백', '십', ''] #돈의 단위 저장, 맨 마지막 일의 자리 뒤에는 아무것도 붙이지 않는다.
    #만약 자릿수가 3자리수가 아닌 천의 자리, 만의 자리 등 더 많이 추가하고 싶은 경우,
    #money_unit 역시 천, 만 등을 추가해야 한다.
    moneyArr = []   # 백의 자리, 십의 자리 ... 등 각 자리 수 저장
    MoneySize = 100 # 돈의 자릿수 = 100의 자리수 -> 만약 세 자리 수가 아닌 더 큰 자리 수를 저장하고 싶으면,
    # MoneySize를 변경한다
    #예를 들어 천의 자리까지 저장하고 싶으면 MoneySize를 1000까지 저장한다.
    unitsize = len(str(MoneySize)) #돈의 자릿수 크기 -> 100이면 3
    resultMessage = "" # 결과를 출력하는 문장

    for i in range(unitsize): #돈의 자릿수 크기만큼 반복
        moneyArr.append(money // MoneySize) #moneyArr 에 money//MoneySize를 나눈 것만큼 저장
        #이를 통해 moneyArr에는 백의 자리, 십의 자리,... 일의 자리 숫자까지 저장된다.
        money %= MoneySize #돈의 자릿수를 MoneySize만큼 날려버린다. 예를 들어 MoneySize가 100이면 백의 자릿수를 날려버린다
        MoneySize //= 10 #반복문 동안 MoneySize는 줄어든다.

    for i in range(len(moneyArr)):
        if moneyArr[i] != 0:
            resultMessage += number_unit[moneyArr[i]] + money_unit[i] + " "
            #money_unit[i]번에 해당하는 한국어를 number_unit에서 찾아 한국어로 변환해 출력한 뒤,
            #단위와 뛰어쓰기를 덧붙인다.
            #각 자릿수 돈이 0이면 아무것도 덧붙이지 않는다.

    return resultMessage.rstrip() + "원" #resultMessage의 맨 오른쪽 뛰어쓰기를 제거한 후 원을 붙여 반환한다.

# 유클리드 호제법을 이용하여 최대공약수를 구하는 함수
# 유클리드 호제법: 두 정수 x, y가 존재할 때, x를 y로 나눈 나머지(x%y)와 y의 최대공약수는 x, y의 최대공약수와 같다.
# -> x%y를 y에 대입하고, 기존 y는 x에 대입하면, 대입 이후 y가 0이 될 때 남은 x가 x, y의 최대공약수이다.
# 예를 들어 10과 12의 최소공약수를 위와 같이 찾아보면
# x = 10, y = 12에서 x % y = 10 % 12 = 2를 y에다가 대입, 그리고 x에다가는 대입 이전 y값인 12 대입
# x = 12, y = 2에서 x % y = 0을 y에다가 대입, 그리고 x에다가는 대입 이전 y값인 2 대입
# y가 0이므로 반복 종료, 최종적으로 x = 2가 최대공약수임
# 만약 x, y가 0보다 작은 음수면 이를 같은 절대값의 양의 정수로 고쳐서 계산한다.
def getGCD(x, y):
    if x < 0:   x *= -1
    if y < 0:   y *= -1 #x, y가 음수면 이를 자동으로 양수로 바꾼다.

    while y != 0:
        x, y = y, x%y
    return x

#자연수를 입력받아 소수인 지를 확인하고, 소수면 True, 소수가 아니면 false를 반환하는 함수
#자연수 N(N>1)을 입력받으면, 2부터 N-1까지 나머지를 구해서, 나머지가 0이 되면 소수가 아니므로 False를 반환한다.
#그렇지 않다면 True를 반환한다.
#만약 N > 1인 자연수가 입력되지 않았다면, 에러를 던진다.
def testPrime(number):
    if number <= 1:
        raise ValueError #자연수가 아니므로 ValueError를 던짐

    for i in range(2, number):
        if number % i == 0:
            return False
            #number를 i로 나눈 나머지가 0이다 -> i는 number의 약수다 ->
            #number는 1이 아닌 다른 자연수를 약수로 가지므로 소수가 아님, False 반환
    #위 반복문을 통과하면 2이상 number - 1 까지 모든 자연수를 다 검사했는데도 약수가 없으므로 소수다.
    #그러므로 True를 반환한다.
    return True


def main():
    #4번 문제를 푼다.
    #점수를 integer형으로 입력받고, 점수에 따라 성적을 알파벳으로 출력한다.
    print("Testing the solution to Problem4 =>")
    score = int(input("Type in a score: "))
    grade = getGrade(score)
    print(f"The grade is {grade} !")
    print('--' * 40)

    #8번 문제를 푼다.
    #1000이하의 금액을 입력받으면, 이를 한국어로 변환해 출력한다.
    #예) 982->구백 팔십 이원, 702-> 칠백 이원 ...
    print("Testing the solution to Problem8 =>")
    n = int(input("1000 이하의 금액을 입력하시오: "))
    moneyText = getMoneyText(n)
    print(moneyText)
    print('--' * 40)

    #9번 문제를 푼다.
    #두 개의 정수를 입력받고, 두 정수의 GCD를 구해 출력한다.
    print("Testing the solution to Problem9 =>")
    x = int(input("Type in the 1st integer: "))
    y = int(input("Type in the 2nd integer: "))
    #유클리드 호제법으로 GCD를 구하는 함수로써,
    #일반적인 gcd 함수에도 x, y가 음의 정수 또는 0인 상황을 예외로 두지 않았기에
    #이 함수도 그 상황에 대한 예외를 두지는 않았다
    result = getGCD(x, y)
    print(f"The GCD between {x} and {y} is {result}!")
    #출력문 맨 마지막의 !은 팩토리얼이 아닌, 매뉴얼에 포함된 강조 문구이다. 혼선이 있을경우 !을 지워야 한다.
    print('--' * 40)

    #10번 문제를 푼다.
    #2이상의 자연수가 소수인지 아닌 지 확인하는 함수로, 이 경우 2이상의 자연수가 아니면 치명적인 오류가 발생할 수 있으므로
    #예외를 일으키도록 처리했다. -> 이때 에러 메시지를 출력한다.
    print("Testing the solution to Problem10 =>")
    for i in range(2, 101): #2부터 100까지 검사
        try:
            if testPrime(i):    #testPrime()의 반환값은 True/False 이기에 if의 조건문으로 직접 쓰일 수 있다.
                print(i, end=" ") #개행을 뛰어쓰기로 바꾸기 위해 end='\n' 대신 end=" "로 바꿔준다.
        except:
            print("1보다 큰 자연수를 입력하지 않았습니다.")

main()
