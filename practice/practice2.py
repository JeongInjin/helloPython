# map 같은거..key 값이 제약이 없는듯 하네..
cabinet = {1: "가가가", 2: "나나나", "3": "다다다"}
print(cabinet)
print(cabinet[1])
print(cabinet[2])
print(cabinet["3"])
print(cabinet.get(1))
print(cabinet.get(2))
print(cabinet.get("3"))
# 대괄호로 가져올경우 key 가 없을경우 exception 이 발생하지만 get 은 None 을 반환한다.
print(cabinet.get(5))
print(cabinet.get(5, "key 값이 없으면 default 값을 줄 수 있다."))

# 값이 있는지 확인
print(1 in cabinet) # True
print(3 in cabinet) # False

cabinet = {"A-1": "AAA", "B-1": "BBB"}
print(cabinet["A-1"])

cabinet["C-1"] = "CCC"
print(cabinet)

del cabinet["A-1"]
print(cabinet)

# key 만 출력
print(cabinet.keys())
# value 만 출력
print(cabinet.values())
# key, value 쌍으로
print(cabinet.items())

cabinet.clear()
print(cabinet)

print("----------------")
# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

(name, age, hobby) = "가나다", 20, "코딩"
print(name, age, hobby)
print("----------------")

















