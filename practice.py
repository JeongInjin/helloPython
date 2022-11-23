# 숫자
print(5)
print(-10)
print(3.14)
print(100_000)
print(5 + 3)
print(2 * 8)
print(3 * (3+1))
print("----------------")
# 문자
print('풍선')
print("풍선")
print("가"*9)
print("----------------")
# boolean
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))
print("----------------")
# variable
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + " 의 이름은" + name + " 예요.")
print(name + "는 " + str(age) + "살이며, " + hobby + "을(를) 아주 좋아해요")
print(name + " 이는 어른이 맞을까요? " + str(is_adult))
print(", 로 할경우 , 다음에 무조건 한칸씩 띄운다.str 로 감싸지 않아도 사용 가능하다.")
print("우리집", animal, "의 이름은", name, "예요.")
print(name, "는", age, "살이며, ", hobby, "을(를) 아주 좋아해요")
print(name, "이는 어른이 맞을까요? ",is_adult)

# 기타

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요" % ("보라", "빨강"))

print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("보라", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("보라", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요".format("보라", "빨강"))


print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "보라"))

#버전 3.6 이상~ 일 경우 아래와 같이 가능
age = 20
color = "초록"
print(f"나는 {age}살이며, {color}색을 좋아해요")


print("----------------")
# 주석부분
'''
여러문장
주석처리는
홀따옴표 3개로 한다.
'''
print("----------------")
print(1+1)
print(3-2)
print(5*2)
print(6/3)
print(2**4) #제곱
print(5%3) #나머지
print(5//3) #몫
print(10//3) #몫

print(3 == 3)
print(4 == 3)
print(3+4 == 7)
print(1 != 3)
print(not (1 != 3))

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True

print(5> 4> 3) #True
print(5> 4> 7) #False

print("----------------")
#숫자처리
print(abs(-5)) #5
print(pow(4, 2)) #4^2 = 16
print(max(5, 12)) #12
print(min(5, 12)) #5
print(round(3.14)) #3 반올림
print(round(4.51)) #5 반올림

from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4
print("----------------")
# 랜덤
from random import *
print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)
print(int(random() * 10)) # 0 ~ 10까지
print(int(random() * 10) + 1) #1 ~10까지

print(int(random() * 45) + 1) #1 ~45
print(randrange(1, 46)) #1 ~ 46미만
print(randint(1, 45)) #1 ~ 45까지

print("----------------")

sentense = '나는 소년입니다.'
print(sentense)
sentense2 = "나는 소년2입니다."
print(sentense2)
sentense3 = """
여러
문자
열
"""
print(sentense3)
print("----------------")
jumin = "980120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일: " + jumin[4:6])
print("생년월: " + jumin[0:6])
print("생년월: " + jumin[:6])

print("뒤 7자리 " + jumin[7:14])
print("뒤 7자리 " + jumin[7:])

print("뒤 7자리(뒤에서부터) " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지
print("----------------")
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) #없으면 -1 값
# print(python.index("Java")) # 없으면 에러.
print(python.count("n"))

print("----------------")
#list
subway = [10, 20, 30]
print(subway)
print(subway[0])

print(subway.index(20))
subway.append(40)
print(subway)
subway.insert(1, 50)
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.append(10)
subway.append(10)
print(subway.count(10)) #갯수 확인

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)


mix_list = ["가", 10, True]
print(mix_list)
num_list = [1, 2, 3]
num_list.extend(mix_list)
print(num_list)

print("----------------")
























