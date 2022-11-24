# if

weather = "비"

if weather == "비":
    print("비비비비비")
elif weather == "미세먼지":
    print("미세먼저")
else:
    print("else.....")

print("----------------")

# input_val = int(input("현재 기온은? "))
# if 30 <= input_val:
#     print("너무 덥네요")
# elif 10 <= input_val and input_val < 30:
#     print("괜찮은 날씨네요")
# elif 0 <= input_val < 10:
#     print("춥네요")
# else:
#     print("너무 춥네요")
print("----------------")

# for
for waiting_no in [0, 1, 2, 3, 4, 5]:
    print("대기번호 : {0}".format(waiting_no))
print("---")

for waiting_no in range(6):
    print("대기번호 : {0}".format(waiting_no))
print("---")
for waiting_no in range(1, 3):
    print("대기번호 : {0}".format(waiting_no))
print("---")


waiting_no = [0, 1, 2, 3, 4, 5]
for no in waiting_no:
    print("대기번호 : {0}".format(no))
print("----------------")

# while
# 파이썬은 증감연산자가 없다.
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# while True:
#     print("무한루프")


print("----------------")
# continue, break
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지 {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
print("----------------")

students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["가", "가나다", "가나"]
print(students)
students = [len(i) for i in students]
print(students)



print("----------------")




