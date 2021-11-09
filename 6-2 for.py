# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
     print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "캡틴아메리카"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))