# 한 줄 처리
print("Python", "Java", sep=" vs ", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 왼, 오 정렬 ljust, rjust
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 001, 002, 003, 004 zfill
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
answer = 10
print(type(answer))
