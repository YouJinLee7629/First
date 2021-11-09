python = "Python is Amazing"
print(python.lower()) #소문자
print(python.upper()) #대문자
print(python[0].isupper()) #True #0번째가 대문자?
print(len(python)) #len=length #17
print(python.replace("Python", "Java"))

index = python.index("n") #몇 번째에 n이 있는지 알려줌
print(index)
index=python.index("n", index+1) #두 번째 n의 위치를 알려줌
print(index)

print(python.find("n"))
print(python.find("Java")) #원하는 값이 없을 경우 결과값은 -1
print(python.index("Java")) #에러

print(python.count("n")) #n이 2번 나옴