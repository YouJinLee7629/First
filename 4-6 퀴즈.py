# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

#예) https://naver.com
#규칙 1) http:// 부분은 제외 => naver.com
#규칙 2) 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙 3) 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                      (nav)         (5)             (1)           (1)

# 예) 생성된 비밀번호 : nav51!

url = "https://naver.com"
my_str = url.replace("https://", "") #규칙1
my_str = my_str[:my_str.index(".")] #규칙2: my_str이라는 변수에 들어가있는 문자열 중에서 . 전까지 
#my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3) 과 같음

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

#url 설정을 바꾸면 다른 비밀번호 값이 나옴