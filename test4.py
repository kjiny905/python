# print('hello')
# #무한루프(종료: ctrl + c)
# while False : 
#     print('hi')

# number = int(input('숫자입력'))
# if number%2 == 0 :
#     print('짝수')
# else :
#     print('홀수')
stop = False
while not stop :
    print('1.저장 2.검색 3.종료')
    menu = int(input('>> '))
    if menu == 1 :
        print('저장')
    elif menu == 2 :
        print('검색')
    elif menu == 3 :
        print('종료')
        break
    else : 
        print('없는 메뉴')

# 2 또는 3으로 나눠지는 수 판단하기
number = 6
if number % 2 == 0 or number % 3 == 0 :
    print('2 또는 3으로 나눠지는 수')
# 2와 3으로 나눠지는 수 판단하기
if number % 2 == 0 and number % 3 == 0 :
    print('2와 3으로 나눠지는 수')

# 함수정의 : 2개의 매개값을 전달받아 합을 구하는 함수
def add(x, y) :
    sum = x + y
    return sum
# 함수호출
result = add(10, 20)
print(result)
