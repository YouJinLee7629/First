# 손님을 5번 부를 때까지 안오면 커피를 폐기처분 시킴
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다")

# 손님이 올때까지 부름 # 무한루프로 반복됨. ctrl + c를 누르면 강제종료
index = 1
customer = "아이언맨"
while True:
    print("{0}님, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
    index += 1

# 이름을 물어보고 커피가 준비가 되었으면 줌
customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}님, 커피가 준비되었습니다.".format(customer, index))
    person = input("이름이 어떻게 되세요?")