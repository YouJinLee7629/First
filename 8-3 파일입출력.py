#1
score_file = open("score.txt", "w", encoding="utf8") # w = 쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

#2
score_file = open("score.txt", "a", encoding="utf8") # a = 덮어쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #\n을 통해 줄바꿈을 해줘야함
score_file.close()

#3
score_file = open("score.txt", "r", encoding="utf8") # r = 읽기
print(score_file.read())
score_file.close()

#4
score_file = open("score.txt", "r", encoding="utf8") # r = 읽기
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

#5
score_file = open("score.txt", "r", encoding="utf8") # 파일이 몇 줄인지 모를 때
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

#6
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()