# set
my_set = {1, 2, 3, 3 ,3}
print(my_set)

java = {"가가가", "나나나", "다다다"}
python = set(["가가가", "라라라"])

print(java & python) # 교집합
print(java.intersection(python)) # 교집합

print(java | python) # 합집합
print(java.union(python)) # 합집합

print(java - python) #차집합
print(java.difference(python)) #차집합

python.add("바바바")
print(python)
java.remove("가가가")
print(java)
print("----------------")

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))


print("----------------")













