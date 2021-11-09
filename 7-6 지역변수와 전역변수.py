# 지역변수
gun = 10 # 10자루

def checkpoint(soldiers): # 경계 근무 나가는 군인 수
    gun = 20 # 함수 내, 외 값이 다름
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무를 나감
print("총 : {0}".format(gun))

# 전역변수
gun = 10 # 10자루

def checkpoint(soldiers): # 경계 근무 나가는 군인 수
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무를 나감
gun = checkpoint_ret(gun, 2)
print("총 : {0}".format(gun))