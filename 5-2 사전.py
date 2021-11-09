cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

# 대괄호를 사용했을 때 없는 값이면 오류, get 소괄호를 사용했을 때 없는 값이면 None을 출력함

print(3 in cabinet) #True
print(5 in cabinet) #False

# 새 손님
print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 둘 다 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)