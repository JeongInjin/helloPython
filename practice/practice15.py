# etc

print(dir([1,2,3,4]))

print(format(1000000000, ","))
print(format(1000000000, "x")) # 16진수
print(format(10000, "0>020,.4f"))

def injin(value):
    if value % 2 == 0:
        return True
    else:
        return False

print(list(filter(injin, range(20))))

print(list(filter(lambda x: x % 2 == 0, range(20))))

print(list(i for i in range(20) if i % 2 == 0))


print(len([1, 2, 3, 4]))

print(list(map(injin, range(20))))
print(list(map(lambda x: x % 2 ==0, range(20))))
print(list(map(lambda x: x ** 2, range(20))))

print(list(zip(['a', 'b', 'c'], [1, 2, 3], [10, 20, 30])))

print(max([1, 2, 3, 4]))
print(min([1, 2, 3, 4]))

testCaseOne = ['abc', 'def', 'hello world', 'hello', 'python']
testCaseTwo = 'Life is too short, You need python'.split()
testCaseThree = list(zip('acbed', [1, 2, 5, 4, 3]))

print(sorted(testCaseOne, key=len, reverse=True))
print(sorted(testCaseTwo, key=str.lower))
print(sorted(testCaseThree, key=lambda x: x[1])) # 1번째 값으로 정렬
print(sorted(testCaseThree, key=lambda x: x[0])) # 0번째 값으로 정렬

print(5 in [1,2,3,4,5])
print(5 not in [1,2,3,4,5])

queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.pop(0)
queue.append(40)
print(queue)

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.pop()
stack.append(40)
print(stack)

d = {"one": "하나", "two": "둘"}
print(d)
print(d.keys())
print(d.values())
print(d.items())
del d["one"]
print(d)
d["one"] = "하나"
print(d)

s = set('11122233343445566')
print(s)
s.add(7)
print(s)
s.discard(7) # 삭제
print(s)
print("1" in s)

판콜에이 = {"A", "B", "C"}
타이레놀 = {"A", "B", "D"}

print(판콜에이.difference(타이레놀)) # 차집합
print(판콜에이.intersection(타이레놀)) # 교집합
print(len(판콜에이.intersection(타이레놀))) # 갯수찾기
print(판콜에이.union(타이레놀)) # 합집합

print(list(map(int, '1 2 3 4 5 6 7 '.split())))

for i in '1 2 3 4 5 6 7'.split():
    print(int(i))

print([int(i) for i in '1 2 3 4 5 6 7 '.split()])















