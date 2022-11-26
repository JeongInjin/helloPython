# 표준 입출력
import sys

print("Kotlin", "Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요")


print("표준 출력", file=sys.stdout)
print("error 출력", file=sys.stderr)
print("----------------")

scores = {"수하": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3))

print("----------------")
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마 찍기
print("{0:,}".format(900000000))
# 3자리 마다 콤마 찍기, +- 부호도 붙이기
print("{0:+,}".format(900000000))
# 3자리 마다 콤마를 찍어주고, 부호도 붙이고, 자릿수 확보하기 빈자리는 ~ 로 채우기
print("{0:~<+30,}".format(99999192923))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지 표시 (소수점 3번째 자리에서 반올림)
print("{0:.2f}".format(5/3))
print("----------------")
